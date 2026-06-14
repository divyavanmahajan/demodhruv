# LLM Trading Bot — Architecture & Technical Reference

> Last updated: 2026-06-14  
> Codebase root: `/home/user/demodhruv`

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [System Architecture](#2-system-architecture)
3. [Component Reference](#3-component-reference)
4. [Data Schemas](#4-data-schemas)
5. [LLM Integration](#5-llm-integration)
6. [Polling & Scheduling](#6-polling--scheduling)
7. [Price Data Pipeline](#7-price-data-pipeline)
8. [Portfolio Engine](#8-portfolio-engine)
9. [Strategy Analysis Pipeline](#9-strategy-analysis-pipeline)
10. [Configuration Reference](#10-configuration-reference)
11. [Extension Points](#11-extension-points)
12. [Known Limitations & Future Work](#12-known-limitations--future-work)

---

## 1. Project Overview

LLM Trading Bot is a **paper-trading simulation** that uses a large language model to make stock buy/sell/hold decisions on a configurable watchlist. It runs as a Streamlit web application with a 15-minute polling loop.

### Key Capabilities

| Capability | Detail |
|---|---|
| Automated trading cycles | LLM consulted every 15 minutes; decisions executed immediately against paper portfolio |
| Dual LLM provider support | Anthropic (Claude Sonnet 4.6) and OpenAI (GPT-4o), switchable from the UI |
| Real-time price data | MarketChameleon web scraping with yfinance fallback |
| Editable strategy prompts | System prompt and user message template editable in-browser, persisted to disk |
| Trade log & analytics | JSON-backed trade log with filter/download UI |
| Strategy analysis | Separate LLM call that analyzes trade history and suggests prompt improvements |
| CSV trade upload | Upload external broker history for LLM analysis alongside or instead of bot history |

### Tech Stack

```
Runtime:         Python 3.11+
UI framework:    Streamlit >= 1.35
LLM providers:   anthropic >= 0.28  |  openai >= 1.30
Price data:      requests + beautifulsoup4 >= 4.12  |  yfinance >= 0.2.40
Data wrangling:  pandas >= 2.0
Persistence:     Local JSON files (no database)
```

---

## 2. System Architecture

### Full Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Streamlit Browser UI                          │
│  Tab 1: Dashboard  │  Tab 2: Trade Log  │  Tab 3: Prompts  │ Tab 4  │
└────────┬───────────┴────────────────────┴──────────────────┴───┬────┘
         │  user action / 30-second sleep+rerun                  │
         ▼                                                        │
┌────────────────────┐                               ┌────────────────────┐
│     app.py         │                               │  analyzer.py       │
│  (orchestrator)    │                               │  Strategy Analysis │
└────────┬───────────┘                               └────────┬───────────┘
         │                                                    │
         │  fetch_prices(watchlist)                           │  analyze_and_suggest()
         ▼                                                    │
┌────────────────────┐                                        │
│  data_fetcher.py   │                                        │
│                    │                                        │
│  1. Scrape         │                                        │
│   marketchameleon  │                                        │
│   .com/Overview/   │                                        │
│   {TICKER}/        │                                        │
│                    │                                        │
│  2. yfinance       │                                        │
│   (fallback)       │                                        │
│                    │                                        │
│  3. {price:0,      │                                        │
│   source:unavail.} │                                        │
└────────┬───────────┘                                        │
         │  prices dict                                       │
         ▼                                                    │
┌────────────────────┐      prompts dict                      │
│   trader.py        │◄── prompts.py ─────────────────────────┤
│  run_trading_cycle │                                        │
│                    │                                        │
│  1. Build prices   │                                        │
│     table string   │                                        │
│  2. Build portfolio│                                        │
│     summary string │                                        │
│  3. Format user    │                                        │
│     message        │                                        │
└────────┬───────────┘                                        │
         │  system_prompt + user_message                      │
         ▼                                                    ▼
┌────────────────────────────────────────────────────────────────────┐
│                          llm_client.py                              │
│                   get_trading_recommendations()                     │
│                                                                     │
│  provider == "anthropic"          provider == "openai"             │
│  ┌─────────────────────┐          ┌─────────────────────┐          │
│  │ anthropic.Anthropic  │          │ openai.OpenAI        │          │
│  │ client.messages      │          │ client.chat.         │          │
│  │ .create(             │          │ completions.create(  │          │
│  │  model=claude-       │          │  model=gpt-4o,       │          │
│  │  sonnet-4-6,         │          │  messages=[system,   │          │
│  │  system=...,         │          │  user],              │          │
│  │  messages=[user])    │          │  max_tokens=1024)    │          │
│  └─────────────────────┘          └─────────────────────┘          │
│                                                                     │
│  Parse response:                                                    │
│    1. json.loads(response_text)                                     │
│    2. re.search(r"\[.*\]", response_text, re.DOTALL) fallback      │
│    3. raise ValueError if both fail                                 │
└────────┬───────────────────────────────────────────────────────────┘
         │  list of recommendation dicts
         ▼
┌────────────────────┐
│   trader.py        │
│  (execute loop)    │
│                    │
│  for each rec:     │
│    BUY → portfolio │
│          .buy()    │
│    SELL→ portfolio │
│          .sell()   │
│    HOLD → skip     │
│    append to log   │
└────────┬───────────┘
         │
         ▼
┌────────────────────────────────────────────────────────────────────┐
│                     portfolio.py + JSON persistence                 │
│                                                                     │
│  portfolio.json          trade_log.json         prompts.json       │
│  (positions + cash)      (all trade records)    (system+template)  │
│                                                                     │
│  trading_bot/data/                                                  │
└────────────────────────────────────────────────────────────────────┘
```

### Module Dependency Graph

```
app.py
  ├── trading_bot/config.py          (constants only, no imports from project)
  ├── trading_bot/portfolio.py       ← config.py
  ├── trading_bot/prompts.py         ← config.py
  ├── trading_bot/data_fetcher.py    (no project imports)
  ├── trading_bot/trader.py          ← config.py, llm_client.py
  └── trading_bot/analyzer.py        ← llm_client.py, config.py (via llm_client)

trading_bot/llm_client.py           ← config.py (lazy, inside functions)
```

---

## 3. Component Reference

### `app.py` — UI Orchestrator

**Purpose:** Top-level Streamlit application. Owns all UI rendering, session state, and wires together the trading pipeline components.

**Session state keys initialized:**

| Key | Type | Meaning |
|---|---|---|
| `last_cycle_time` | `datetime \| None` | Timestamp of last trading cycle run |
| `last_cycle_result` | `dict \| None` | Full result dict from `run_trading_cycle()` |
| `prices` | `dict` | Last fetched prices dict |
| `prices_fetched_at` | `datetime \| None` | When prices were last fetched |
| `analysis_result` | `str \| None` | Last LLM strategy analysis text |
| `analysis_time` | `datetime \| None` | When analysis was run |
| `analysis_source` | `str \| None` | Description of data source used |

**Tabs:**

| Tab | Title | Key responsibility |
|---|---|---|
| 1 | Dashboard | Portfolio metrics, positions table, watchlist prices, cycle trigger, auto-rerun loop |
| 2 | Trade Log | Filterable trade history table, summary stats, CSV download |
| 3 | Prompt Editor | Edit/save/reset system prompt and user template |
| 4 | Strategy Analysis | Configure history source, run LLM analysis, view suggestions |

**Notable functions:**

- `should_auto_cycle() -> bool` — Returns `True` if `POLL_INTERVAL_SECONDS` have elapsed since `last_cycle_time`.
- `get_prices(tickers) -> dict` — Calls `fetch_prices()` and stores result + timestamp in session state.
- `load_trade_log() -> list` — Reads `TRADE_LOG_FILE` from disk or returns `[]`.
- `_pnl_html(val, prefix) -> str` — Returns colored HTML span for P&L display.

---

### `trading_bot/config.py` — Configuration Constants

**Purpose:** Single source of truth for all configurable constants and environment-derived settings. No business logic.

See [Section 10](#10-configuration-reference) for full table.

---

### `trading_bot/portfolio.py` — Portfolio Engine

**Purpose:** Manages paper-trading positions and cash. Performs buy/sell execution, P&L calculations, and JSON persistence.

**Class:** `Portfolio(cash: float, positions: dict)`

| Method | Signature | Returns |
|---|---|---|
| `load` (classmethod) | `() -> Portfolio` | Loads from `portfolio.json` or creates fresh with `STARTING_CASH` |
| `save` | `()` | Writes current state to `portfolio.json` |
| `buy` | `(ticker, shares, price) -> dict` | Executes buy, updates positions, returns trade record |
| `sell` | `(ticker, shares, price) -> dict` | Executes sell with realized P&L, returns trade record |
| `total_value` | `(prices: dict) -> float` | Cash + sum of market values of all positions |
| `unrealized_pnl` | `(prices: dict) -> dict` | `{ticker: unrealized_pnl_float}` for each position |
| `portfolio_summary` | `(prices: dict) -> str` | Formatted ASCII table string for LLM context injection |

See [Section 8](#8-portfolio-engine) for calculation details.

---

### `trading_bot/data_fetcher.py` — Price Data Pipeline

**Purpose:** Fetches current stock prices from MarketChameleon (primary) or yfinance (fallback).

**Public interface:**

```python
fetch_prices(tickers: list) -> dict
# Returns: {"AAPL": {"price": 189.42, "change_pct": 1.23, "source": "marketchameleon"}, ...}
```

**Private functions:**

- `_scrape_marketchameleon(ticker: str) -> dict | None`
- `_fetch_yfinance(ticker: str) -> dict | None`

See [Section 7](#7-price-data-pipeline) for full pipeline details.

---

### `trading_bot/llm_client.py` — LLM Interface

**Purpose:** Thin adapter over Anthropic and OpenAI Python SDKs. Sends prompts, receives JSON, handles parsing.

**Public interface:**

```python
get_trading_recommendations(
    system_prompt: str,
    user_message: str,
    provider: str,       # "anthropic" | "openai"
    api_key: str,
) -> list                # list of recommendation dicts
```

**Raises:** `ValueError` if no API key, unknown provider, or JSON cannot be parsed.

See [Section 5](#5-llm-integration) for full detail.

---

### `trading_bot/trader.py` — Trading Cycle Runner

**Purpose:** Orchestrates one complete trading cycle: builds LLM context, calls LLM, executes trades, appends to trade log.

**Public interface:**

```python
run_trading_cycle(
    portfolio: Portfolio,
    prices: dict,
    prompts: dict,
    provider: str,
    api_key: str,
) -> dict   # {"recommendations": list, "trades_executed": list, "errors": list, "timestamp": str}
```

**Private functions:**

- `_build_prices_table(prices: dict) -> str` — Formats prices into a fixed-width ASCII table for LLM injection.
- `_load_trade_log() -> list` — Reads trade log from disk.
- `_save_trade_log(log: list)` — Persists trade log to disk.

**Trade record shape written to log:**

```python
{
    "timestamp": "2026-06-14T10:30:00.123456",
    "ticker": "AAPL",
    "action": "BUY",                # or "SELL", "HOLD", "HOLD (buy failed)", "HOLD (sell failed)"
    "quantity": 10,
    "price": 189.42,
    "rationale": "Strong upward momentum...",
    "portfolio_value_after": 98234.50,   # None for HOLD
    "error": None,                       # or error string if execution failed
    "realized_pnl": 234.50,             # only present on SELL
}
```

---

### `trading_bot/prompts.py` — Prompt Management

**Purpose:** Loads, saves, and resets the LLM system prompt and user message template. Provides hardcoded defaults.

**Public interface:**

```python
load_prompts() -> dict           # {"system": str, "user_template": str}
save_prompts(prompts: dict)      # writes to PROMPTS_FILE
reset_prompts() -> dict          # restores defaults, writes to disk, returns dict
```

**Default system prompt rules (embedded in `DEFAULT_SYSTEM_PROMPT`):**

1. Never invest more than 20% of total portfolio value in a single stock
2. Prefer momentum: buy stocks trending up over the last session
3. Take profits when a position gains more than 15%
4. Cut losses when a position drops more than 8%
5. Keep at least 20% of portfolio in cash as a buffer
6. Consider time of day (avoid trades in first/last 15 min of market hours)

**Default user template placeholders:**

- `{prices_table}` — replaced by output of `_build_prices_table()`
- `{portfolio_summary}` — replaced by output of `portfolio.portfolio_summary()`

---

### `trading_bot/analyzer.py` — Strategy Analyzer

**Purpose:** Builds a trade performance summary and sends it to the LLM for strategy improvement suggestions. Also provides CSV column normalization for uploaded trade files.

**Public interface:**

```python
analyze_and_suggest(
    trade_log: list,
    prompts: dict,
    provider: str,
    api_key: str,
) -> str    # plain-text numbered recommendations from LLM

normalize_uploaded_row(row: dict) -> dict
# Normalizes one CSV row dict to internal trade record format
```

**Module-level constant:** `ANALYZER_SYSTEM_PROMPT` — instructs the LLM to act as a quantitative strategy analyst and return plain text numbered recommendations.

See [Section 9](#9-strategy-analysis-pipeline) for full details.

---

## 4. Data Schemas

All data files live under `trading_bot/data/` (created at import time by `config.py`).

### `portfolio.json`

```json
{
  "cash": 87340.50,
  "positions": {
    "AAPL": {
      "shares": 25,
      "avg_cost": 182.34
    },
    "NVDA": {
      "shares": 10,
      "avg_cost": 875.00
    }
  }
}
```

| Field | Type | Description |
|---|---|---|
| `cash` | `float` | Available paper cash in USD |
| `positions` | `object` | Map of ticker → position object |
| `positions[ticker].shares` | `int` | Number of shares held |
| `positions[ticker].avg_cost` | `float` | Volume-weighted average purchase price per share |

**Initial state** (no file on disk): `cash = 100000.0`, `positions = {}`

---

### `trade_log.json`

An ordered JSON array. Each element is a trade record:

```json
[
  {
    "timestamp": "2026-06-14T10:30:01.234567",
    "ticker": "AAPL",
    "action": "BUY",
    "quantity": 10,
    "price": 189.42,
    "rationale": "Strong upward momentum, below 20% portfolio limit.",
    "portfolio_value_after": 99812.30,
    "error": null
  },
  {
    "timestamp": "2026-06-14T10:45:02.987654",
    "ticker": "AAPL",
    "action": "SELL",
    "quantity": 10,
    "price": 192.10,
    "rationale": "Position gained >15%, taking profits.",
    "portfolio_value_after": 101923.50,
    "error": null,
    "realized_pnl": 26.80
  },
  {
    "timestamp": "2026-06-14T11:00:00.112233",
    "ticker": "MSFT",
    "action": "HOLD",
    "quantity": 0,
    "price": 415.30,
    "rationale": "No clear signal.",
    "portfolio_value_after": null,
    "error": null
  }
]
```

| Field | Type | Always present | Description |
|---|---|---|---|
| `timestamp` | `string (ISO 8601)` | yes | Cycle timestamp (all recs in one cycle share same value) |
| `ticker` | `string` | yes | Stock ticker symbol |
| `action` | `string` | yes | `BUY`, `SELL`, `HOLD`, `HOLD (buy failed)`, `HOLD (sell failed)` |
| `quantity` | `int` | yes | Shares transacted (0 for HOLD) |
| `price` | `float` | yes | Price at time of recommendation (from prices dict) |
| `rationale` | `string` | yes | One-sentence LLM justification |
| `portfolio_value_after` | `float \| null` | yes | Total portfolio value after trade; null for HOLDs |
| `error` | `string \| null` | yes | Error message if execution failed; null otherwise |
| `realized_pnl` | `float` | SELL only | Realized profit/loss: `(price - avg_cost) × shares` |

---

### `prompts.json`

```json
{
  "system": "You are an expert stock trader running a dry-run simulation...",
  "user_template": "Current market data:\n{prices_table}\n\nMy current portfolio:\n{portfolio_summary}\n\nBased on your trading strategy, what should I do with each ticker? Respond ONLY with a JSON array."
}
```

| Field | Type | Description |
|---|---|---|
| `system` | `string` | LLM system prompt defining trading personality and rules |
| `user_template` | `string` | User message template; must contain `{prices_table}` and `{portfolio_summary}` |

If `prompts.json` does not exist, defaults from `prompts.py` are used in-memory (file is only written on explicit save or reset).

---

## 5. LLM Integration

### Provider Support

| Provider | SDK | Model | Config constant |
|---|---|---|---|
| `anthropic` | `anthropic >= 0.28` | `claude-sonnet-4-6` | `ANTHROPIC_MODEL` |
| `openai` | `openai >= 1.30` | `gpt-4o` | `OPENAI_MODEL` |

The provider and API key are selected from the Streamlit sidebar and passed down through `run_trading_cycle()` → `get_trading_recommendations()`.

### Message Format Sent to LLM

**Anthropic call:**
```python
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=system_prompt,           # trading strategy rules
    messages=[
        {"role": "user", "content": user_message}   # prices table + portfolio
    ],
)
```

**OpenAI call:**
```python
client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_message},
    ],
    max_tokens=1024,
)
```

### User Message Content (at runtime)

The user message is the `user_template` from `prompts.json` with two substitutions:

1. `{prices_table}` → output of `_build_prices_table(prices)`:

```
Ticker       Price    Change%           Source
------------------------------------------------
AAPL        189.42      +1.23%   marketchameleon
MSFT        415.30      -0.45%          yfinance
```

2. `{portfolio_summary}` → output of `portfolio.portfolio_summary(prices)`:

```
Cash: $87,340.50
Total Portfolio Value: $99,925.50

Ticker     Shares   Avg Cost    Current    Mkt Value        P&L
------------------------------------------------------------
AAPL           25     182.34     189.42     4735.50      178.00
```

### Expected LLM Response Format

The LLM is instructed to return **only** a raw JSON array (no markdown fences, no explanation):

```json
[
  {"ticker": "AAPL", "action": "BUY",  "quantity": 10, "rationale": "Strong momentum."},
  {"ticker": "MSFT", "action": "HOLD", "quantity": 0,  "rationale": "No clear signal."},
  {"ticker": "GOOGL","action": "SELL", "quantity": 5,  "rationale": "Taking profits at +17%."}
]
```

### JSON Extraction and Error Handling (`llm_client.py`)

Three-step parse sequence:

```
Step 1: json.loads(response_text)
           ↓ success → return list
           ↓ JSONDecodeError

Step 2: re.search(r"\[.*\]", response_text, re.DOTALL)
        json.loads(match.group())
           ↓ success → return list
           ↓ no match or JSONDecodeError

Step 3: raise ValueError("Could not parse JSON from LLM response:\n{first 500 chars}")
```

The regex fallback (Step 2) handles cases where the model wraps its JSON in markdown code fences or adds preamble text before the array.

### Strategy Analysis LLM Call

`analyze_and_suggest()` in `analyzer.py` makes a **separate** LLM call using `ANALYZER_SYSTEM_PROMPT` (not the trading system prompt). It requests **plain text** output (not JSON), so no JSON parsing is needed — the raw `response_text` is returned directly. `max_tokens=2048` (versus `1024` for trading cycles).

---

## 6. Polling & Scheduling

### The 15-Minute Cycle

There is no background thread or scheduler. The polling loop is implemented entirely within Streamlit's rendering model using `time.sleep()` + `st.rerun()`.

**Sequence in `app.py` Tab 1 (lines 243–248):**

```python
if api_key and st.session_state["last_cycle_time"]:
    elapsed = (datetime.now() - st.session_state["last_cycle_time"]).total_seconds()
    if elapsed < POLL_INTERVAL_SECONDS:
        time.sleep(30)       # block this Streamlit script thread for 30 seconds
        st.rerun()           # force a full script re-execution
```

**Effect:** After any page render where a cycle has run but the next 15-minute window has not elapsed, the app sleeps 30 seconds (blocking the server-side script) then re-renders the whole page. This creates a polling loop with ~30-second granularity.

**Auto-cycle trigger check (lines 87–91):**

```python
def should_auto_cycle():
    if not st.session_state["last_cycle_time"]:
        return False
    elapsed = (datetime.now() - st.session_state["last_cycle_time"]).total_seconds()
    return elapsed >= POLL_INTERVAL_SECONDS   # POLL_INTERVAL_SECONDS = 900
```

The `should_auto_cycle()` check fires in the normal render path at line 152:

```python
if run_now or (api_key and should_auto_cycle()):
    ...
    result = run_trading_cycle(...)
    st.session_state["last_cycle_time"] = datetime.now()
```

### Price Caching

Prices are **not** re-fetched on every 30-second rerun. They are only fetched when:

1. `fetch_now` button is clicked (explicit user action)
2. `st.session_state["prices"]` is empty (first load)
3. A trading cycle is triggered and `prices` is empty at that moment

```python
if fetch_now or not st.session_state["prices"]:
    prices = get_prices(watchlist)
else:
    prices = st.session_state["prices"]   # use cached
```

The age of cached prices is displayed as: `"Prices last fetched: HH:MM:SS"`.

### First-Cycle Behavior

On initial load with no prior cycle (`last_cycle_time = None`):
- `should_auto_cycle()` returns `False`
- The 30-second sleep loop is **not** entered (condition `api_key and st.session_state["last_cycle_time"]` is falsy)
- The user must manually click "Run Trading Cycle Now" to start the loop
- After the first manual cycle, the auto-loop kicks in

---

## 7. Price Data Pipeline

### URL Pattern and Scraping Approach

Primary source: `https://marketchameleon.com/Overview/{TICKER}/`

The scraper uses a Chrome desktop `User-Agent` header to avoid basic bot detection:

```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ..."
}
```

**CSS selectors tried in order:**

```python
[
    ".stock-price",
    ".quote-price",
    ".last-price",
    "[class*='price']",
    "[class*='Price']",
]
```

For each selector, the element's text is stripped of `$` and `,`, then a `\d+\.\d+` regex extracts the numeric value.

**Regex page-scan fallback** (if all selectors fail):

```python
matches = re.findall(r"\$(\d{1,5}\.\d{2})", soup.get_text())
if matches:
    price = float(matches[0])   # takes first match
```

**Change percent selectors tried:**

```python
["[class*='change']", "[class*='Change']", ".pct-change"]
```

Extracts `([+-]?\d+\.\d+)%` from element text.

### yfinance Fallback

Called when `_scrape_marketchameleon()` returns `None`:

```python
t = yf.Ticker(ticker)
info = t.fast_info
price = info.get("last_price") or info.get("regularMarketPrice")
prev  = info.get("previous_close")
change_pct = ((price - prev) / prev * 100) if price and prev else 0.0
```

Uses `fast_info` (lighter than `info` which makes multiple network calls).

### 1-Second Delay

`time.sleep(1)` is called between each ticker in `fetch_prices()` to avoid rate-limiting on MarketChameleon.

### Returned Dict Shape

```python
{
    "AAPL": {
        "price": 189.42,          # float, 0.0 if unavailable
        "change_pct": 1.23,       # float, 0.0 if unavailable
        "source": "marketchameleon"  # | "yfinance" | "unavailable"
    },
    ...
}
```

The `"unavailable"` sentinel is used when both data sources fail, allowing the rest of the pipeline to continue with a zero price.

---

## 8. Portfolio Engine

### Data Model

```
Portfolio
  cash: float                  — undeployed paper money
  positions: dict              — {ticker: {shares: int, avg_cost: float}}
```

Persisted as `portfolio.json` after every `buy()` or `sell()` call (immediate write, no buffering).

### Buy Execution (`portfolio.buy`)

1. Validates `shares > 0`
2. Computes `cost = shares × price`
3. Validates `cost <= self.cash`
4. If position exists: **volume-weighted average cost** recalculation:
   ```
   new_avg_cost = (existing_shares × existing_avg_cost + new_shares × price)
                  / (existing_shares + new_shares)
   ```
5. If no position: creates `{shares: shares, avg_cost: price}`
6. Deducts `cost` from `self.cash`
7. Calls `self.save()`
8. Returns trade record dict

### Sell Execution (`portfolio.sell`)

1. Validates `shares > 0`
2. Validates ticker exists and `available_shares >= shares`
3. Computes:
   ```
   proceeds     = shares × price
   realized_pnl = (price - avg_cost) × shares
   ```
4. Reduces `positions[ticker].shares` by `shares`
5. If `shares == 0` after reduction: **deletes the position key entirely**
6. Adds `proceeds` to `self.cash`
7. Calls `self.save()`
8. Returns trade record dict including `realized_pnl`

### Total Value Calculation

```
total_value = cash + Σ (positions[ticker].shares × prices[ticker].price)
```

Tickers in `positions` that are **not** in `prices` dict contribute `0` to the sum (silent omission, not an error).

### Unrealized P&L

```
unrealized_pnl[ticker] = (current_price - avg_cost) × shares
```

Only computed for tickers present in both `positions` and `prices`.

### Portfolio Summary String

Generated by `portfolio_summary(prices)` for LLM injection. Fixed-width ASCII table:

```
Cash: $87,340.50
Total Portfolio Value: $99,925.50

Ticker     Shares   Avg Cost    Current    Mkt Value        P&L
------------------------------------------------------------
AAPL           25     182.34     189.42     4735.50      178.00
NVDA           10     875.00     920.15     9201.50      451.50
No open positions.    ← shown instead of table rows when positions is empty
```

### Cash Management Rules (from LLM System Prompt)

These are enforced by LLM instruction, **not** by the portfolio engine itself:
- Maximum 20% of total portfolio value in a single stock
- Minimum 20% of portfolio value held as cash buffer

The portfolio engine will execute any trade the LLM recommends as long as cash/share constraints are arithmetically satisfied.

---

## 9. Strategy Analysis Pipeline

### Three Source Modes

Selected via radio button in Tab 4:

| Mode | `analysis_log` value | `source_label` |
|---|---|---|
| Bot's own trade history | `internal_log` | `"bot history (N trades)"` |
| Upload my own CSV | `uploaded_log` | `"uploaded CSV (N trades)"` |
| Merge both | `internal_log + uploaded_log` | `"merged (N bot + M uploaded trades)"` |

### CSV Column Normalization (`normalize_uploaded_row`)

Applies to each row of an uploaded CSV before it is added to `analysis_log`. Column name mapping (case-insensitive, spaces→underscores):

| CSV column name(s) | Internal field |
|---|---|
| `date`, `time`, `datetime` | `timestamp` |
| `symbol`, `stock` | `ticker` |
| `side`, `type`, `transaction` | `action` |
| `shares`, `qty`, `units` | `quantity` |
| `cost`, `fill_price`, `exec_price` | `price` |
| `pnl`, `profit`, `gain_loss` | `realized_pnl` |
| `notes`, `comment`, `reason` | `rationale` |

Action value normalization: `"B"` → `"BUY"`, `"S"` → `"SELL"`, `"H"` → `"HOLD"`. Already-canonical values pass through unchanged.

Numeric fields (`quantity`, `price`, `realized_pnl`) have `$` and `,` stripped before `float()` conversion. Missing fields default to `0.0`.

Uploaded rows are tagged with `"_source": "uploaded"`.

### Performance Summary Built for LLM

`analyze_and_suggest()` computes from the trade log:

```
Total cycles analyzed:  (unique timestamps)
Total BUY trades:       N
Total SELL trades:      N
Win rate on sells:      X.X%
Total realized P&L:     $X,XXX.XX

P&L by ticker:
  AAPL: $234.50
  NVDA: -$89.00

Recent trades (last 20):
  [2026-06-14T10:30] AAPL BUY 10sh @ $189.42 — Strong momentum...

Current system prompt being used:
  <full system prompt text>
```

This summary is sent as the user message with the `ANALYZER_SYSTEM_PROMPT` system prompt. The LLM returns plain text numbered recommendations (not JSON). `max_tokens=2048`.

---

## 10. Configuration Reference

File: `trading_bot/config.py`

| Constant | Type | Default | What it controls |
|---|---|---|---|
| `DEFAULT_WATCHLIST` | `list[str]` | `["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]` | Tickers shown in sidebar; used for price fetching and LLM context |
| `STARTING_CASH` | `float` | `100_000.0` | Initial paper cash; also used as denominator in total P&L % calculation in UI |
| `POLL_INTERVAL_SECONDS` | `int` | `900` (15 min) | Seconds between automatic trading cycles |
| `LLM_PROVIDER` | `str` | `os.getenv("LLM_PROVIDER", "anthropic")` | Default LLM provider (overridden by sidebar selection) |
| `ANTHROPIC_API_KEY` | `str` | `os.getenv("ANTHROPIC_API_KEY", "")` | Pre-filled value for Anthropic key in sidebar |
| `OPENAI_API_KEY` | `str` | `os.getenv("OPENAI_API_KEY", "")` | Pre-filled value for OpenAI key in sidebar |
| `ANTHROPIC_MODEL` | `str` | `"claude-sonnet-4-6"` | Anthropic model ID used for both trading and analysis calls |
| `OPENAI_MODEL` | `str` | `"gpt-4o"` | OpenAI model ID used for both trading and analysis calls |
| `DATA_DIR` | `str` | `<module_dir>/data/` | Directory for all JSON persistence files; created at import time |
| `PORTFOLIO_FILE` | `str` | `<DATA_DIR>/portfolio.json` | Portfolio state persistence path |
| `TRADE_LOG_FILE` | `str` | `<DATA_DIR>/trade_log.json` | Trade history persistence path |
| `PROMPTS_FILE` | `str` | `<DATA_DIR>/prompts.json` | Custom prompt persistence path |

`DATA_DIR` is resolved relative to the `trading_bot/` package directory using `os.path.dirname(__file__)`, making the data path stable regardless of working directory.

---

## 11. Extension Points

### Adding a New LLM Provider

1. **`trading_bot/config.py`** — Add a model constant, e.g. `GEMINI_MODEL = "gemini-pro"`.

2. **`trading_bot/llm_client.py`** — Add an `elif provider == "gemini":` branch inside `get_trading_recommendations()`:
   ```python
   elif provider == "gemini":
       import google.generativeai as genai
       genai.configure(api_key=api_key)
       model = genai.GenerativeModel(GEMINI_MODEL)
       resp = model.generate_content(system_prompt + "\n\n" + user_message)
       response_text = resp.text
   ```
   The existing three-step JSON parse (lines 45–58) handles the result automatically.

3. **`trading_bot/analyzer.py`** — Add the same `elif provider == "gemini":` branch inside `analyze_and_suggest()`.

4. **`app.py`** — Add `"gemini"` to the `st.selectbox("LLM Provider", [...])` list and add a key input row.

### Adding a New Price Data Source

1. **`trading_bot/data_fetcher.py`** — Add a new private function `_fetch_newsource(ticker: str) -> dict | None` following the return shape `{"price": float, "change_pct": float, "source": str}`.

2. In `fetch_prices()`, insert the new source in the fallback chain:
   ```python
   data = _scrape_marketchameleon(ticker)
   if data is None:
       data = _fetch_newsource(ticker)       # ← new fallback
   if data is None:
       data = _fetch_yfinance(ticker)
   ```

### Adding a New UI Tab

1. **`app.py`** — Add the tab label to the `st.tabs([...])` call and unpack the new variable:
   ```python
   tab1, tab2, tab3, tab4, tab5 = st.tabs([..., "🆕 New Tab"])
   ```

2. Add a `with tab5:` block implementing the tab content. Session state keys for the new tab follow the existing pattern of initializing to `None` in the `# Session state init` block at the top of `app.py`.

---

## 12. Known Limitations & Future Work

### Market Hours Detection

The system prompt instructs the LLM to "avoid trades in first/last 15 min of market hours," but this is LLM judgment only — there is no programmatic market-hours check. The bot will run cycles and execute trades 24/7, including weekends and after-hours. Prices returned during closed markets may be stale or zero.

**Future work:** Add a `is_market_open()` guard in `run_trading_cycle()` using `pandas_market_calendars` or the NYSE calendar. Optionally skip cycle or change LLM instruction based on market status.

### Scraping Fragility

MarketChameleon's HTML structure is not under our control. The CSS selectors in `_scrape_marketchameleon()` are heuristic and will break if the site changes class names. The regex fallback (`re.findall(r"\$(\d{1,5}\.\d{2})", text)`) picks the first dollar-amount on the page, which may not be the current price.

**Future work:** Use a paid market data API (Polygon.io, Alpha Vantage, Tiingo) as primary source. Keep yfinance as secondary. Remove web scraping entirely.

### Streamlit Threading Constraints

The 30-second `time.sleep(30)` in the auto-rerun loop blocks the Streamlit script-runner thread. With multiple concurrent browser sessions, each session's sleep blocks a thread. Under high concurrency this could exhaust the thread pool.

**Future work:** Use `streamlit-autorefresh` component or `st.fragment` with a timer to avoid blocking. Alternatively, externalize the trading loop to a background process (e.g., APScheduler, Celery) that writes results to disk, and have Streamlit just poll results.

### Trade Log Write Pattern

`_save_trade_log()` in `trader.py` re-writes the entire log file on every recommendation (including HOLDs). For a large log this is inefficient and creates a window for data loss.

**Future work:** Append-only JSONL format, or SQLite for proper concurrent access.

### No Partial-Share Support

`portfolio.buy()` accepts `shares: int`. The LLM may recommend fractional quantities; these are coerced to `int` via `int(rec.get("quantity", 0))` in `trader.py` (line 58), silently truncating.

**Future work:** Support fractional shares or add an explicit validation/rounding step with a log warning.

### API Key Security

API keys are entered in a Streamlit text input with `type="password"` and stored only in Streamlit session state (in-memory per session). They are never written to disk. However, they transit the Streamlit WebSocket unencrypted if TLS is not configured.

**Future work:** Load keys exclusively from environment variables or a secrets manager; remove the key input from the sidebar UI for production deployments.

### No Realized P&L on BUY Records

BUY trade records in `trade_log.json` do not store `realized_pnl` (it is a SELL-only field). The trade log `realized_pnl` sum in the UI's trade log summary (Tab 2) correctly filters to SELL-only rows.
