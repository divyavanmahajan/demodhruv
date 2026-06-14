import time
import json
import os
from datetime import datetime, timedelta

import streamlit as st
import pandas as pd

from trading_bot.config import (
    DEFAULT_WATCHLIST, STARTING_CASH, POLL_INTERVAL_SECONDS,
    ANTHROPIC_API_KEY, OPENAI_API_KEY, TRADE_LOG_FILE
)
from trading_bot.portfolio import Portfolio
from trading_bot.prompts import load_prompts, save_prompts, reset_prompts
from trading_bot.data_fetcher import fetch_prices
from trading_bot.trader import run_trading_cycle
from trading_bot.analyzer import analyze_and_suggest

st.set_page_config(page_title="LLM Trading Bot", page_icon="📈", layout="wide")

# ── Session state init ──────────────────────────────────────────────────────
if "last_cycle_time" not in st.session_state:
    st.session_state["last_cycle_time"] = None
if "last_cycle_result" not in st.session_state:
    st.session_state["last_cycle_result"] = None
if "prices" not in st.session_state:
    st.session_state["prices"] = {}
if "prices_fetched_at" not in st.session_state:
    st.session_state["prices_fetched_at"] = None
if "analysis_result" not in st.session_state:
    st.session_state["analysis_result"] = None
if "analysis_time" not in st.session_state:
    st.session_state["analysis_time"] = None

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ Configuration")

    provider = st.selectbox("LLM Provider", ["anthropic", "openai"], index=0)
    default_key = ANTHROPIC_API_KEY if provider == "anthropic" else OPENAI_API_KEY
    api_key = st.text_input("API Key", value=default_key, type="password")

    watchlist_str = st.text_area(
        "Watchlist (comma-separated)",
        value=", ".join(DEFAULT_WATCHLIST),
        height=80,
    )
    watchlist = [t.strip().upper() for t in watchlist_str.split(",") if t.strip()]

    st.divider()

    # Next cycle countdown
    if st.session_state["last_cycle_time"]:
        elapsed = (datetime.now() - st.session_state["last_cycle_time"]).total_seconds()
        remaining = max(0, POLL_INTERVAL_SECONDS - elapsed)
        mins, secs = divmod(int(remaining), 60)
        st.metric("Next auto-cycle in", f"{mins:02d}:{secs:02d}")
    else:
        st.info("No cycle run yet")

    st.divider()

    if st.button("🔄 Reset Portfolio", type="secondary"):
        st.session_state["confirm_reset"] = True

    if st.session_state.get("confirm_reset"):
        st.warning("This will wipe all positions and reset cash to $100,000. Are you sure?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, reset", type="primary"):
                p = Portfolio(STARTING_CASH, {})
                p.save()
                if os.path.exists(TRADE_LOG_FILE):
                    os.remove(TRADE_LOG_FILE)
                st.session_state["confirm_reset"] = False
                st.session_state["last_cycle_result"] = None
                st.success("Portfolio reset!")
                st.rerun()
        with col2:
            if st.button("Cancel"):
                st.session_state["confirm_reset"] = False
                st.rerun()

# ── Auto-cycle check ─────────────────────────────────────────────────────────
def should_auto_cycle():
    if not st.session_state["last_cycle_time"]:
        return False
    elapsed = (datetime.now() - st.session_state["last_cycle_time"]).total_seconds()
    return elapsed >= POLL_INTERVAL_SECONDS

def _pnl_color(val):
    if val > 0:
        return "green"
    elif val < 0:
        return "red"
    return "gray"

def _pnl_html(val, prefix="$"):
    color = _pnl_color(val)
    sign = "+" if val > 0 else ""
    return f'<span style="color:{color}">{sign}{prefix}{val:,.2f}</span>'

# ── Fetch prices helper ──────────────────────────────────────────────────────
def get_prices(tickers):
    with st.spinner("Fetching prices..."):
        prices = fetch_prices(tickers)
    st.session_state["prices"] = prices
    st.session_state["prices_fetched_at"] = datetime.now()
    return prices

# ── Load trade log ───────────────────────────────────────────────────────────
def load_trade_log():
    if os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "r") as f:
            return json.load(f)
    return []

# ── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📋 Trade Log", "✏️ Prompt Editor", "🔬 Strategy Analysis"])

# ════════════════════════════════════════════════════════════════════════════
# TAB 1: Dashboard
# ════════════════════════════════════════════════════════════════════════════
with tab1:
    st.header("📈 LLM Trading Bot — Dashboard")

    if not api_key:
        st.warning("⚠️ No API key set. Enter your API key in the sidebar to enable trading cycles.")

    col_run, col_fetch, col_auto = st.columns([2, 2, 3])

    with col_run:
        run_now = st.button("▶️ Run Trading Cycle Now", type="primary", disabled=not api_key)
    with col_fetch:
        fetch_now = st.button("🔄 Refresh Prices")
    with col_auto:
        auto_label = "🟢 Auto-cycle ON (15 min)" if api_key else "🔴 Auto-cycle OFF (no API key)"
        st.caption(auto_label)

    # Fetch prices if needed
    if fetch_now or not st.session_state["prices"]:
        prices = get_prices(watchlist)
    else:
        prices = st.session_state["prices"]

    portfolio = Portfolio.load()
    prompts = load_prompts()

    # Run cycle
    if run_now or (api_key and should_auto_cycle()):
        if not prices:
            prices = get_prices(watchlist)
        with st.spinner("Asking LLM for trade recommendations..."):
            result = run_trading_cycle(portfolio, prices, prompts, provider, api_key)
        st.session_state["last_cycle_result"] = result
        st.session_state["last_cycle_time"] = datetime.now()
        portfolio = Portfolio.load()  # reload after trades

    # ── Metrics ─────────────────────────────────────────────────────────────
    total_val = portfolio.total_value(prices)
    pnl = total_val - STARTING_CASH
    pnl_pct = (pnl / STARTING_CASH) * 100

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("💼 Portfolio Value", f"${total_val:,.2f}")
    m2.metric("💵 Cash", f"${portfolio.cash:,.2f}")
    pnl_delta = f"+${pnl:,.2f}" if pnl >= 0 else f"-${abs(pnl):,.2f}"
    m3.metric("📈 Total P&L", pnl_delta, delta=f"{pnl_pct:+.2f}%")
    m4.metric("📦 Open Positions", len(portfolio.positions))

    if st.session_state["prices_fetched_at"]:
        st.caption(f"Prices last fetched: {st.session_state['prices_fetched_at'].strftime('%H:%M:%S')}")

    st.divider()

    # ── Positions table ──────────────────────────────────────────────────────
    st.subheader("Open Positions")
    if portfolio.positions:
        rows = []
        for ticker, pos in portfolio.positions.items():
            price = prices.get(ticker, {}).get("price", 0)
            mkt_val = pos["shares"] * price
            upnl = (price - pos["avg_cost"]) * pos["shares"]
            upnl_pct = ((price - pos["avg_cost"]) / pos["avg_cost"] * 100) if pos["avg_cost"] else 0
            rows.append({
                "Ticker": ticker,
                "Shares": pos["shares"],
                "Avg Cost": f"${pos['avg_cost']:.2f}",
                "Current Price": f"${price:.2f}",
                "Market Value": f"${mkt_val:,.2f}",
                "Unrealized P&L": f"${upnl:+,.2f}",
                "P&L %": f"{upnl_pct:+.2f}%",
            })
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No open positions. Run a trading cycle to get recommendations.")

    st.divider()

    # ── Current prices ───────────────────────────────────────────────────────
    st.subheader("Watchlist Prices")
    if prices:
        price_rows = []
        for ticker in watchlist:
            d = prices.get(ticker, {"price": 0, "change_pct": 0, "source": "N/A"})
            price_rows.append({
                "Ticker": ticker,
                "Price": f"${d['price']:.2f}",
                "Change %": f"{d['change_pct']:+.2f}%",
                "Source": d["source"],
            })
        st.dataframe(pd.DataFrame(price_rows), use_container_width=True, hide_index=True)

    # ── Last cycle result ────────────────────────────────────────────────────
    result = st.session_state.get("last_cycle_result")
    if result:
        st.divider()
        st.subheader(f"Last Cycle — {result['timestamp'][:19]}")

        if result["errors"]:
            for e in result["errors"]:
                st.warning(f"⚠️ {e}")

        recs = result.get("recommendations", [])
        if recs:
            rec_rows = []
            for r in recs:
                action = r.get("action", "HOLD")
                color = {"BUY": "🟢", "SELL": "🔴", "HOLD": "⚪"}.get(action, "⚪")
                rec_rows.append({
                    "": color,
                    "Ticker": r.get("ticker", ""),
                    "Action": action,
                    "Qty": r.get("quantity", 0),
                    "Rationale": r.get("rationale", ""),
                })
            st.dataframe(pd.DataFrame(rec_rows), use_container_width=True, hide_index=True)

    # ── Auto-rerun ───────────────────────────────────────────────────────────
    if api_key and st.session_state["last_cycle_time"]:
        elapsed = (datetime.now() - st.session_state["last_cycle_time"]).total_seconds()
        if elapsed < POLL_INTERVAL_SECONDS:
            # Schedule a rerun when the interval elapses (check every 30s)
            time.sleep(30)
            st.rerun()

# ════════════════════════════════════════════════════════════════════════════
# TAB 2: Trade Log
# ════════════════════════════════════════════════════════════════════════════
with tab2:
    st.header("📋 Trade Log")

    log = load_trade_log()

    if not log:
        st.info("No trades yet. Run a trading cycle to see history here.")
    else:
        df_log = pd.DataFrame(log)
        df_log["timestamp"] = pd.to_datetime(df_log["timestamp"])

        # Filters
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            date_filter = st.selectbox("Filter", ["Today", "This Month", "All Time"], index=0)
        with filter_col2:
            action_filter = st.multiselect("Actions", ["BUY", "SELL", "HOLD"], default=["BUY", "SELL", "HOLD"])

        now = datetime.now()
        if date_filter == "Today":
            mask = df_log["timestamp"].dt.date == now.date()
        elif date_filter == "This Month":
            mask = (df_log["timestamp"].dt.year == now.year) & (df_log["timestamp"].dt.month == now.month)
        else:
            mask = pd.Series([True] * len(df_log))

        action_mask = df_log["action"].isin(action_filter)
        filtered = df_log[mask & action_mask].copy()

        # Summary stats
        sells_f = filtered[filtered["action"] == "SELL"]
        realized = sells_f["realized_pnl"].sum() if "realized_pnl" in sells_f.columns else 0
        winning = (sells_f["realized_pnl"] > 0).sum() if "realized_pnl" in sells_f.columns else 0
        win_rate = (winning / len(sells_f) * 100) if len(sells_f) > 0 else 0

        s1, s2, s3, s4 = st.columns(4)
        s1.metric("Total Trades", len(filtered))
        s2.metric("Buys", len(filtered[filtered["action"] == "BUY"]))
        s3.metric("Sells", len(sells_f))
        s4.metric("Realized P&L", f"${realized:+,.2f}")

        if len(sells_f) > 0:
            st.caption(f"Win rate: {win_rate:.1f}% ({winning}/{len(sells_f)} sells profitable)")

        st.divider()

        display_cols = ["timestamp", "ticker", "action", "quantity", "price"]
        if "realized_pnl" in filtered.columns:
            display_cols.append("realized_pnl")
        display_cols.append("rationale")

        st.dataframe(
            filtered[display_cols].sort_values("timestamp", ascending=False),
            use_container_width=True,
            hide_index=True,
        )

# ════════════════════════════════════════════════════════════════════════════
# TAB 3: Prompt Editor
# ════════════════════════════════════════════════════════════════════════════
with tab3:
    st.header("✏️ Trading Strategy Prompts")
    st.info(
        "The **system prompt** defines the LLM's trading personality and rules. "
        "The **user template** is sent each cycle with live data injected at "
        "`{prices_table}` and `{portfolio_summary}`."
    )

    prompts = load_prompts()

    system_prompt_input = st.text_area(
        "System Prompt (trading strategy)", value=prompts["system"], height=300
    )
    user_template_input = st.text_area(
        "User Message Template", value=prompts["user_template"], height=150
    )

    p1, p2 = st.columns(2)
    with p1:
        if st.button("💾 Save Prompts", type="primary"):
            if "{prices_table}" not in user_template_input or "{portfolio_summary}" not in user_template_input:
                st.error("User template must contain {prices_table} and {portfolio_summary}")
            else:
                save_prompts({"system": system_prompt_input, "user_template": user_template_input})
                st.success("Prompts saved!")
    with p2:
        if st.button("↩️ Reset to Defaults"):
            reset_prompts()
            st.success("Prompts reset to defaults!")
            st.rerun()

# ════════════════════════════════════════════════════════════════════════════
# TAB 4: Strategy Analysis
# ════════════════════════════════════════════════════════════════════════════
with tab4:
    st.header("🔬 Strategy Analysis & Prompt Improvement")
    st.write(
        "Send your trade history to the LLM and get specific suggestions for improving "
        "your trading strategy prompt."
    )

    if not api_key:
        st.warning("⚠️ Enter an API key in the sidebar to use this feature.")
    else:
        if st.button("🧠 Analyze My Trading Strategy", type="primary"):
            log = load_trade_log()
            prompts = load_prompts()
            with st.spinner("Analyzing trading performance..."):
                suggestion = analyze_and_suggest(log, prompts, provider, api_key)
            st.session_state["analysis_result"] = suggestion
            st.session_state["analysis_time"] = datetime.now()

        if st.session_state.get("analysis_result"):
            st.caption(f"Analysis run at: {st.session_state['analysis_time'].strftime('%Y-%m-%d %H:%M:%S')}")
            st.divider()
            st.markdown("### LLM Suggestions")
            st.markdown(
                f"""<div style="background:#1e2130;padding:1.2rem;border-radius:8px;
                border-left:4px solid #4CAF50;font-family:monospace;font-size:0.9rem;
                white-space:pre-wrap">{st.session_state['analysis_result']}</div>""",
                unsafe_allow_html=True,
            )
            if st.button("📋 Apply Suggestions to System Prompt"):
                st.info("Review the suggestions above and manually paste them into the Prompt Editor tab, then save.")
