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


def _scrape_marketchameleon(ticker: str) -> dict | None:
    url = f"https://marketchameleon.com/Overview/{ticker}/"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Try common price selectors
        price = None
        change_pct = None

        for selector in [
            ".stock-price", ".quote-price", ".last-price",
            "[class*='price']", "[class*='Price']"
        ]:
            el = soup.select_one(selector)
            if el:
                text = el.get_text(strip=True).replace("$", "").replace(",", "")
                m = re.search(r"\d+\.\d+", text)
                if m:
                    price = float(m.group())
                    break

        # Fallback: regex scan the full page text for a price pattern near ticker
        if price is None:
            text = soup.get_text()
            # Look for $ followed by a number
            matches = re.findall(r"\$(\d{1,5}\.\d{2})", text)
            if matches:
                price = float(matches[0])

        # Try to find % change
        for selector in ["[class*='change']", "[class*='Change']", ".pct-change"]:
            el = soup.select_one(selector)
            if el:
                text = el.get_text(strip=True)
                m = re.search(r"([+-]?\d+\.\d+)%", text)
                if m:
                    change_pct = float(m.group(1))
                    break

        if price:
            return {"price": price, "change_pct": change_pct or 0.0, "source": "marketchameleon"}
    except Exception as e:
        print(f"[data_fetcher] Marketchameleon error for {ticker}: {e}", file=sys.stderr)
    return None


def _fetch_yfinance(ticker: str) -> dict | None:
    try:
        import yfinance as yf
        t = yf.Ticker(ticker)
        info = t.fast_info
        price = info.get("last_price") or info.get("regularMarketPrice")
        prev = info.get("previous_close")
        change_pct = ((price - prev) / prev * 100) if price and prev else 0.0
        if price:
            return {"price": float(price), "change_pct": float(change_pct), "source": "yfinance"}
    except Exception as e:
        print(f"[data_fetcher] yfinance error for {ticker}: {e}", file=sys.stderr)
    return None


def fetch_prices(tickers: list) -> dict:
    results = {}
    for ticker in tickers:
        data = _scrape_marketchameleon(ticker)
        if data is None:
            print(f"[data_fetcher] Falling back to yfinance for {ticker}", file=sys.stderr)
            data = _fetch_yfinance(ticker)
        if data is None:
            data = {"price": 0.0, "change_pct": 0.0, "source": "unavailable"}
        results[ticker] = data
        time.sleep(1)
    return results
