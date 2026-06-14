import re
import time
import sys
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def _fetch_yfinance(ticker: str) -> dict | None:
    try:
        import yfinance as yf
        t = yf.Ticker(ticker)
        info = t.fast_info
        # fast_info returns camelCase attribute-style access
        price = getattr(info, "last_price", None) or getattr(info, "regularMarketPrice", None)
        prev = getattr(info, "previous_close", None) or getattr(info, "regularMarketPreviousClose", None)
        change_pct = ((price - prev) / prev * 100) if price and prev else 0.0
        if price:
            return {"price": float(price), "change_pct": float(change_pct), "source": "yfinance"}
    except Exception as e:
        print(f"[data_fetcher] yfinance error for {ticker}: {e}", file=sys.stderr)
    return None


def _scrape_marketchameleon(ticker: str) -> dict | None:
    """
    Marketchameleon uses JavaScript rendering — a plain HTTP GET returns a
    mostly-empty shell page. We attempt the scrape anyway and fall back to
    yfinance if no price is found.
    """
    url = f"https://marketchameleon.com/Overview/{ticker}/"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        price = None
        change_pct = None

        for selector in [
            ".stock-price", ".quote-price", ".last-price",
            "[class*='stockprice']", "[class*='lastprice']",
            "[class*='price']", "[class*='Price']",
            "span.val", "td.val",
        ]:
            el = soup.select_one(selector)
            if el:
                text = el.get_text(strip=True).replace("$", "").replace(",", "")
                m = re.search(r"\d{1,5}\.\d{2}", text)
                if m:
                    price = float(m.group())
                    break

        # Regex scan full page text for dollar amounts
        if price is None:
            text = soup.get_text()
            matches = re.findall(r"\$(\d{1,5}\.\d{2})", text)
            if matches:
                price = float(matches[0])

        for selector in ["[class*='change']", "[class*='Change']", ".pct-change"]:
            el = soup.select_one(selector)
            if el:
                m = re.search(r"([+-]?\d+\.\d+)%", el.get_text(strip=True))
                if m:
                    change_pct = float(m.group(1))
                    break

        if price:
            return {"price": price, "change_pct": change_pct or 0.0, "source": "marketchameleon"}
    except Exception as e:
        print(f"[data_fetcher] Marketchameleon error for {ticker}: {e}", file=sys.stderr)
    return None


def fetch_prices(tickers: list) -> dict:
    """
    Fetch current prices for a list of tickers.
    Primary: yfinance (reliable, real-time).
    Secondary: Marketchameleon scrape (attempted but often blocked by JS rendering).
    Sentinel on total failure: price=0.0, source="unavailable".
    """
    results = {}
    for ticker in tickers:
        # yfinance is the reliable primary; Marketchameleon scrape is opportunistic
        data = _fetch_yfinance(ticker)
        if data is None:
            print(f"[data_fetcher] yfinance failed for {ticker}, trying Marketchameleon", file=sys.stderr)
            data = _scrape_marketchameleon(ticker)
        if data is None:
            print(f"[data_fetcher] All sources failed for {ticker}", file=sys.stderr)
            data = {"price": 0.0, "change_pct": 0.0, "source": "unavailable"}
        results[ticker] = data
        time.sleep(0.5)
    return results
