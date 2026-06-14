from datetime import datetime
from trading_bot.llm_client import get_trading_recommendations


ANALYZER_SYSTEM_PROMPT = """You are a quantitative trading strategy analyst. 
Analyze the provided trading history and performance metrics, then suggest specific, 
actionable improvements to the trading strategy prompt. Focus on:
- Win rate and what's causing losses
- Position sizing issues
- Timing patterns (when trades succeed vs fail)
- Which tickers performed best/worst
- Specific prompt language that should be added, changed, or removed

Be concrete and specific. Output plain text with numbered recommendations."""


def normalize_uploaded_row(row: dict) -> dict:
    """Map common CSV column names to the internal trade record format."""
    mapping = {
        "date": "timestamp", "time": "timestamp", "datetime": "timestamp",
        "symbol": "ticker", "stock": "ticker",
        "side": "action", "type": "action", "transaction": "action",
        "shares": "quantity", "qty": "quantity", "units": "quantity",
        "cost": "price", "fill_price": "price", "exec_price": "price",
        "pnl": "realized_pnl", "profit": "realized_pnl", "gain_loss": "realized_pnl",
        "notes": "rationale", "comment": "rationale", "reason": "rationale",
    }
    normalized = {}
    for k, v in row.items():
        key = k.strip().lower().replace(" ", "_")
        normalized[mapping.get(key, key)] = v

    # Normalize action values to BUY/SELL/HOLD
    action = str(normalized.get("action", "HOLD")).strip().upper()
    for alias, canonical in [("B", "BUY"), ("S", "SELL"), ("H", "HOLD"), ("BUY", "BUY"), ("SELL", "SELL")]:
        if action == alias:
            action = canonical
            break
    normalized["action"] = action

    # Ensure numeric fields
    for field in ("quantity", "price", "realized_pnl"):
        try:
            normalized[field] = float(str(normalized.get(field, 0)).replace(",", "").replace("$", "") or 0)
        except ValueError:
            normalized[field] = 0.0

    normalized.setdefault("ticker", "UNKNOWN")
    normalized.setdefault("timestamp", datetime.now().isoformat())
    normalized.setdefault("rationale", "(uploaded)")
    normalized["_source"] = "uploaded"
    return normalized


def analyze_and_suggest(trade_log: list, prompts: dict, provider: str, api_key: str) -> str:
    if not trade_log:
        return "No trade history to analyze yet. Run some trading cycles first."

    # Build performance summary
    buys = [t for t in trade_log if t.get("action") == "BUY"]
    sells = [t for t in trade_log if t.get("action") == "SELL"]
    total_realized = sum(t.get("realized_pnl", 0) for t in sells)
    winning_sells = [t for t in sells if t.get("realized_pnl", 0) > 0]
    win_rate = (len(winning_sells) / len(sells) * 100) if sells else 0

    ticker_pnl = {}
    for t in sells:
        ticker = t.get("ticker", "?")
        ticker_pnl[ticker] = ticker_pnl.get(ticker, 0) + t.get("realized_pnl", 0)

    summary_lines = [
        f"Total cycles analyzed: {len(set(t['timestamp'] for t in trade_log))}",
        f"Total BUY trades: {len(buys)}",
        f"Total SELL trades: {len(sells)}",
        f"Win rate on sells: {win_rate:.1f}%",
        f"Total realized P&L: ${total_realized:,.2f}",
        "",
        "P&L by ticker:",
    ]
    for ticker, pnl in sorted(ticker_pnl.items(), key=lambda x: x[1], reverse=True):
        summary_lines.append(f"  {ticker}: ${pnl:,.2f}")

    summary_lines += [
        "",
        "Recent trades (last 20):",
    ]
    for t in trade_log[-20:]:
        summary_lines.append(
            f"  [{t.get('timestamp','?')[:16]}] {t.get('ticker','?')} {t.get('action','?')} "
            f"{t.get('quantity',0)}sh @ ${t.get('price',0):.2f} — {t.get('rationale','')}"
        )

    summary_lines += [
        "",
        "Current system prompt being used:",
        prompts.get("system", "(none)"),
    ]

    user_message = "\n".join(summary_lines)
    user_message += "\n\nPlease analyze this trading performance and suggest specific improvements to the trading strategy prompt."

    try:
        # For analysis we want a text response, so we use a different approach
        if provider == "anthropic":
            import anthropic
            from trading_bot.config import ANTHROPIC_MODEL
            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(
                model=ANTHROPIC_MODEL,
                max_tokens=2048,
                system=ANALYZER_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_message}],
            )
            return msg.content[0].text
        elif provider == "openai":
            import openai
            from trading_bot.config import OPENAI_MODEL
            client = openai.OpenAI(api_key=api_key)
            resp = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": ANALYZER_SYSTEM_PROMPT},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=2048,
            )
            return resp.choices[0].message.content
    except Exception as e:
        return f"Analysis failed: {e}"
