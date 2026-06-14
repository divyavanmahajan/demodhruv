import json
import os
from trading_bot.config import PROMPTS_FILE

DEFAULT_SYSTEM_PROMPT = """You are an expert stock trader running a dry-run simulation. You must respond ONLY with valid JSON — no markdown, no explanation, just a raw JSON array.

Your trading rules:
- Never invest more than 20% of total portfolio value in a single stock
- Prefer momentum: buy stocks trending up over the last session
- Take profits when a position gains more than 15%
- Cut losses when a position drops more than 8%
- Keep at least 20% of portfolio in cash as a buffer
- Consider the current time of day (avoid trades in first/last 15 min of market hours)

Respond with a JSON array of objects, one per ticker. Each object must have:
  - "ticker": string
  - "action": "BUY" | "SELL" | "HOLD"
  - "quantity": integer (shares to buy/sell; 0 for HOLD)
  - "rationale": string (one sentence)

Example:
[
  {"ticker": "AAPL", "action": "BUY", "quantity": 10, "rationale": "Strong upward momentum, below 20% portfolio limit."},
  {"ticker": "MSFT", "action": "HOLD", "quantity": 0, "rationale": "No clear signal, maintaining position."}
]"""

DEFAULT_USER_TEMPLATE = """Current market data:
{prices_table}

My current portfolio:
{portfolio_summary}

Based on your trading strategy, what should I do with each ticker? Respond ONLY with a JSON array."""


def load_prompts() -> dict:
    if os.path.exists(PROMPTS_FILE):
        with open(PROMPTS_FILE, "r") as f:
            return json.load(f)
    return {"system": DEFAULT_SYSTEM_PROMPT, "user_template": DEFAULT_USER_TEMPLATE}


def save_prompts(prompts: dict):
    with open(PROMPTS_FILE, "w") as f:
        json.dump(prompts, f, indent=2)


def reset_prompts():
    defaults = {"system": DEFAULT_SYSTEM_PROMPT, "user_template": DEFAULT_USER_TEMPLATE}
    save_prompts(defaults)
    return defaults
