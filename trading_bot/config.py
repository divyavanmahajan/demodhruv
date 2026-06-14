import os

DEFAULT_WATCHLIST = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
STARTING_CASH = 100_000.0
POLL_INTERVAL_SECONDS = 15 * 60

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "anthropic")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_MODEL = "claude-sonnet-4-6"
OPENAI_MODEL = "gpt-4o"

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

PORTFOLIO_FILE = os.path.join(DATA_DIR, "portfolio.json")
TRADE_LOG_FILE = os.path.join(DATA_DIR, "trade_log.json")
PROMPTS_FILE = os.path.join(DATA_DIR, "prompts.json")
