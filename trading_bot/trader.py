import json
import os
from datetime import datetime
from trading_bot.config import TRADE_LOG_FILE
from trading_bot.llm_client import get_trading_recommendations


def _load_trade_log() -> list:
    if os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "r") as f:
            return json.load(f)
    return []


def _save_trade_log(log: list):
    with open(TRADE_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


def _build_prices_table(prices: dict) -> str:
    lines = [f"{'Ticker':<8} {'Price':>10} {'Change%':>10} {'Source':>16}"]
    lines.append("-" * 48)
    for ticker, data in prices.items():
        lines.append(
            f"{ticker:<8} {data['price']:>10.2f} {data['change_pct']:>9.2f}% {data['source']:>16}"
        )
    return "\n".join(lines)


def run_trading_cycle(portfolio, prices: dict, prompts: dict, provider: str, api_key: str) -> dict:
    timestamp = datetime.now().isoformat()
    prices_table = _build_prices_table(prices)
    portfolio_summary = portfolio.portfolio_summary(prices)

    user_message = prompts["user_template"].format(
        prices_table=prices_table,
        portfolio_summary=portfolio_summary,
    )

    errors = []
    trades_executed = []
    recommendations = []

    try:
        recommendations = get_trading_recommendations(
            system_prompt=prompts["system"],
            user_message=user_message,
            provider=provider,
            api_key=api_key,
        )
    except Exception as e:
        errors.append(f"LLM error: {e}")
        return {"recommendations": [], "trades_executed": [], "errors": errors, "timestamp": timestamp}

    for rec in recommendations:
        ticker = rec.get("ticker", "")
        action = rec.get("action", "HOLD").upper()
        quantity = int(rec.get("quantity", 0))
        rationale = rec.get("rationale", "")
        price = prices.get(ticker, {}).get("price", 0.0)

        trade_record = {
            "timestamp": timestamp,
            "ticker": ticker,
            "action": action,
            "quantity": quantity,
            "price": price,
            "rationale": rationale,
            "portfolio_value_after": None,
            "error": None,
        }

        if action == "BUY" and quantity > 0 and price > 0:
            try:
                portfolio.buy(ticker, quantity, price)
                trade_record["portfolio_value_after"] = portfolio.total_value(prices)
                trades_executed.append(trade_record)
            except ValueError as e:
                trade_record["error"] = str(e)
                trade_record["action"] = "HOLD (buy failed)"
                errors.append(f"{ticker}: {e}")
        elif action == "SELL" and quantity > 0 and price > 0:
            try:
                result = portfolio.sell(ticker, quantity, price)
                trade_record["realized_pnl"] = result.get("realized_pnl", 0)
                trade_record["portfolio_value_after"] = portfolio.total_value(prices)
                trades_executed.append(trade_record)
            except ValueError as e:
                trade_record["error"] = str(e)
                trade_record["action"] = "HOLD (sell failed)"
                errors.append(f"{ticker}: {e}")

        # Log all recs (including HOLDs) to trade log
        log = _load_trade_log()
        log.append(trade_record)
        _save_trade_log(log)

    return {
        "recommendations": recommendations,
        "trades_executed": trades_executed,
        "errors": errors,
        "timestamp": timestamp,
    }
