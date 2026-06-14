# LLM Trading Bot — Product Specification

> Last updated: 2026-06-14  
> Codebase root: `/home/user/demodhruv`

---

## Table of Contents

1. [Product Requirements](#1-product-requirements)
2. [Non-Functional Requirements](#2-non-functional-requirements)
3. [User Stories](#3-user-stories)
4. [Acceptance Criteria](#4-acceptance-criteria)
5. [Out of Scope](#5-out-of-scope)

---

## 1. Product Requirements

### Functional Requirements

**Price Data**

1. The system SHALL fetch current stock prices for a user-configurable list of tickers.
2. The system SHALL attempt to fetch prices from MarketChameleon as the primary source.
3. The system SHALL fall back to yfinance if MarketChameleon fails for a given ticker.
4. The system SHALL report `price=0.0` and `source="unavailable"` if both sources fail, without halting the cycle.
5. The system SHALL display the data source (`marketchameleon`, `yfinance`, or `unavailable`) for each ticker in the UI.
6. The system SHALL display the timestamp of the last price fetch.

**Trading Cycle**

7. The system SHALL send current prices and portfolio state to an LLM on each cycle.
8. The system SHALL support Anthropic (Claude Sonnet 4.6) and OpenAI (GPT-4o) as LLM providers, selectable from the UI.
9. The system SHALL parse the LLM's JSON response and execute BUY, SELL, or HOLD actions accordingly.
10. The system SHALL automatically run trading cycles at a configurable interval (default: 15 minutes) when an API key is present.
11. The system SHALL allow the user to manually trigger a trading cycle at any time.
12. The system SHALL display a countdown to the next scheduled cycle in the sidebar.
13. The system SHALL gracefully handle LLM API errors by logging the error and skipping trade execution for that cycle.
14. The system SHALL attempt to extract a JSON array from LLM responses that contain surrounding text (markdown fences, preamble).

**Portfolio Management**

15. The system SHALL maintain a paper portfolio starting with $100,000 in cash and no positions.
16. The system SHALL execute buys using a volume-weighted average cost method when adding to existing positions.
17. The system SHALL calculate realized P&L on each sell as `(sell_price - avg_cost) × shares`.
18. The system SHALL reject buy orders that exceed available cash and log the failure without crashing.
19. The system SHALL reject sell orders for shares not held and log the failure without crashing.
20. The system SHALL persist portfolio state to disk after every trade execution.
21. The system SHALL allow the user to reset the portfolio to its initial state ($100,000 cash, no positions) with a confirmation step.
22. The system SHALL display total portfolio value, cash balance, total P&L, and number of open positions as headline metrics.
23. The system SHALL display a table of open positions with shares, average cost, current price, market value, unrealized P&L, and P&L percentage.

**Trade Log**

24. The system SHALL record every LLM recommendation (BUY, SELL, and HOLD) to a persistent trade log.
25. The system SHALL record the ticker, action, quantity, price, rationale, timestamp, and post-trade portfolio value for each log entry.
26. The system SHALL record realized P&L for SELL entries.
27. The system SHALL allow the user to filter the trade log by date range (Today / This Month / All Time) and by action type.
28. The system SHALL display summary statistics: total trades, buys, sells, realized P&L, and win rate.
29. The system SHALL allow the user to download filtered trade history as a CSV file.

**Prompt Management**

30. The system SHALL have a default system prompt encoding trading rules and a default user message template.
31. The system SHALL allow the user to edit the system prompt and user message template in the browser.
32. The system SHALL persist custom prompts to disk so they survive page reloads.
33. The system SHALL validate that the user template contains `{prices_table}` and `{portfolio_summary}` before saving.
34. The system SHALL allow the user to reset prompts to built-in defaults with a single click.

**Strategy Analysis**

35. The system SHALL allow the user to request an LLM analysis of trade history to receive strategy improvement suggestions.
36. The system SHALL support three analysis history sources: bot's own trade log, an uploaded CSV file, or a merge of both.
37. The system SHALL normalize uploaded CSV files with flexible column names to the internal trade record format.
38. The system SHALL include total trades, win rate, realized P&L, per-ticker P&L, and the last 20 trades in the analysis context.
39. The system SHALL include the currently active system prompt in the analysis context.
40. The system SHALL display the LLM's analysis suggestions as plain text in the UI.

---

## 2. Non-Functional Requirements

### Performance

| Requirement | Target |
|---|---|
| Price fetch latency per ticker | ≤ 10 seconds (includes 1-second inter-ticker delay) |
| Total price fetch for 5-ticker default watchlist | ≤ 60 seconds |
| LLM trading cycle response time | Dependent on LLM API; no hard limit, displayed with spinner |
| UI responsiveness during price fetch / LLM call | Streamlit spinner shown; UI blocked until complete |
| Trade log read/write | < 1 second for logs up to ~10,000 entries |

### Reliability

- The system must not crash if any single ticker's price fetch fails; errors are logged to stderr and the ticker gets a zero-price sentinel.
- The system must not crash if the LLM returns malformed JSON; the error is captured in the cycle result's `errors` list and shown in the UI.
- The system must not crash if a recommended trade is arithmetically impossible (insufficient cash or shares); the failure is logged as `HOLD (buy/sell failed)`.
- Portfolio state is written atomically via `json.dump` on every trade; a crash mid-cycle will at most lose the in-progress cycle's state.

### Security

- API keys are accepted via a `type="password"` Streamlit text input (masked in the browser).
- API keys are pre-populated from environment variables `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` if set; otherwise the field is blank.
- API keys are stored only in Streamlit session state (in-memory per browser session) and are never written to disk.
- No authentication layer is provided; the application assumes a trusted-network or single-user deployment.
- All data files (`portfolio.json`, `trade_log.json`, `prompts.json`) are plain text with no encryption.

---

## 3. User Stories

1. **As a retail investor**, I want to watch an LLM make paper trades on my watchlist so that I can evaluate whether its strategy would be profitable before risking real money.

2. **As a user**, I want to switch between Anthropic and OpenAI without restarting the application so that I can compare the trading decisions of different LLM providers side-by-side.

3. **As a power user**, I want to edit the LLM's system prompt directly in the browser so that I can customize the trading rules (stop-loss thresholds, position size limits, preferred strategies) without touching code.

4. **As a user**, I want the bot to run automatically every 15 minutes so that I do not have to manually trigger each cycle while I am doing other work.

5. **As a user**, I want to see a countdown to the next cycle in the sidebar so that I know when the next trade decisions will be made and do not have to guess.

6. **As a user**, I want to download my bot's trade history as a CSV so that I can do my own analysis in Excel or a Jupyter notebook.

7. **As an active trader**, I want to upload my own broker's trade history CSV and have the LLM analyze it alongside the bot's history so that I can get unified strategy feedback on both paper and live trades.

8. **As a user**, I want the LLM to tell me specifically what to change in the system prompt after reviewing my trade history so that I can iteratively improve the bot's strategy without guessing what to adjust.

9. **As a developer evaluating the system**, I want to reset the portfolio back to $100,000 with a single click so that I can start a clean test without manually deleting data files.

10. **As a user**, I want to see the source of each price (MarketChameleon vs yfinance vs unavailable) in the watchlist table so that I know how reliable the data is before trusting a trading decision based on it.

---

## 4. Acceptance Criteria

### AC-1: Automated 15-Minute Trading Cycle

**Done when:**
- [ ] With a valid API key entered, after the first manual cycle completes, subsequent cycles fire automatically without user interaction.
- [ ] The sidebar countdown decrements from 15:00 toward 00:00 and resets after each cycle.
- [ ] With no API key, the sidebar shows "Auto-cycle OFF" and no cycles run automatically.
- [ ] Manual "Run Trading Cycle Now" button is disabled when no API key is entered.

### AC-2: LLM Trade Execution

**Done when:**
- [ ] A BUY recommendation results in a position being created or increased in the portfolio.
- [ ] A SELL recommendation reduces or closes a position and records realized P&L.
- [ ] A HOLD recommendation is logged to the trade log but does not change portfolio state.
- [ ] A BUY that exceeds available cash is rejected; the entry in the trade log shows `action: "HOLD (buy failed)"` and the error message.
- [ ] A SELL for more shares than held is rejected; the entry shows `action: "HOLD (sell failed)"`.
- [ ] LLM API errors show a warning in the Dashboard and do not corrupt portfolio state.

### AC-3: Price Data Pipeline

**Done when:**
- [ ] Prices are fetched for all tickers in the watchlist on first load and on "Refresh Prices" click.
- [ ] A ticker that fails MarketChameleon scraping falls back to yfinance without error.
- [ ] A ticker that fails both sources shows `source: "unavailable"` and `price: $0.00` in the UI, without halting other tickers.
- [ ] The timestamp "Prices last fetched: HH:MM:SS" updates each time prices are refreshed.

### AC-4: Portfolio Persistence

**Done when:**
- [ ] After a trade executes, `portfolio.json` is updated immediately.
- [ ] After a page refresh (browser reload), the portfolio state is restored from disk.
- [ ] The "Reset Portfolio" button wipes `portfolio.json` and `trade_log.json` after a two-step confirmation, restoring $100,000 cash and zero positions.

### AC-5: Prompt Editor

**Done when:**
- [ ] Changes made in the Prompt Editor tab and saved via "Save Prompts" are used in the very next trading cycle.
- [ ] Saving a user template without `{prices_table}` or `{portfolio_summary}` shows an error and does not save.
- [ ] "Reset to Defaults" restores the original built-in system prompt and user template.
- [ ] After a page refresh, custom prompts are restored from `prompts.json`.

### AC-6: Trade Log Filtering & Download

**Done when:**
- [ ] "Today" filter shows only trades where the timestamp date equals today's date.
- [ ] "This Month" filter shows trades in the current calendar month.
- [ ] Action filter (BUY/SELL/HOLD multiselect) correctly restricts displayed rows.
- [ ] Realized P&L summary stat sums only SELL-action rows within the filtered set.
- [ ] "Download trade history as CSV" downloads a valid CSV with the filtered rows.

### AC-7: Strategy Analysis — Uploaded CSV

**Done when:**
- [ ] An uploaded CSV with standard column names (`timestamp`, `ticker`, `action`, `quantity`, `price`) is loaded without error.
- [ ] An uploaded CSV with alternate column names (`date`, `symbol`, `side`, `shares`, `fill_price`) is normalized and loaded without error.
- [ ] After uploading, a preview of the first 5 rows is shown.
- [ ] "Merge both" mode sends combined bot + uploaded trades to the LLM.
- [ ] The LLM's strategy suggestions are displayed as styled text in the UI.

---

## 5. Out of Scope

The following are explicitly **not** part of this system's requirements:

| Item | Reason excluded |
|---|---|
| **Real money trading** | The system is a paper-trading simulation only. No broker API integration exists or is planned. |
| **Real broker integration** | No connection to Interactive Brokers, Alpaca, TD Ameritrade, Robinhood, or any brokerage API. |
| **Order types beyond market orders** | Limit orders, stop-loss orders, trailing stops, and options are not modeled. All executions use the price-at-recommendation-time as a synthetic fill. |
| **Multi-user support** | No authentication, user accounts, or per-user portfolio isolation. Single-user deployment only. |
| **Portfolio database** | Persistence uses local JSON files. No SQL, NoSQL, or cloud database is used or supported. |
| **Historical backtesting** | No ability to replay historical price data to evaluate strategy performance on past data. |
| **Technical indicators** | No MACD, RSI, Bollinger Bands, or other computed indicators are fed to the LLM. Only price and change% are provided. |
| **News/sentiment data** | No news feed, earnings calendar, or social sentiment data is included in LLM context. |
| **Market hours enforcement** | The system does not programmatically detect market open/close. It relies on the LLM prompt instruction to avoid off-hours trades. |
| **Tax lot accounting** | FIFO, LIFO, or specific-lot P&L calculation is not implemented. Only volume-weighted average cost is tracked. |
| **Short selling** | Only long positions are supported. Selling shares not held is rejected as an error. |
| **Dividend/split adjustments** | Corporate actions (stock splits, dividends) are not modeled or adjusted for. |
| **Alerting / notifications** | No email, SMS, Slack, or push notifications when a trade executes or a cycle completes. |
| **Audit trail / versioning** | Prompt changes are not versioned; the previous prompt is overwritten on save. |
| **Mobile-responsive UI** | The Streamlit layout uses `layout="wide"` and is optimized for desktop browsers only. |
