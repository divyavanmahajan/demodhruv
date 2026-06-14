import json
import os
from datetime import datetime
from trading_bot.config import PORTFOLIO_FILE, STARTING_CASH


class Portfolio:
    def __init__(self, cash: float, positions: dict):
        self.cash = cash
        self.positions = positions  # {ticker: {"shares": int, "avg_cost": float}}

    @classmethod
    def load(cls) -> "Portfolio":
        if os.path.exists(PORTFOLIO_FILE):
            with open(PORTFOLIO_FILE, "r") as f:
                data = json.load(f)
            return cls(data["cash"], data["positions"])
        return cls(STARTING_CASH, {})

    def save(self):
        with open(PORTFOLIO_FILE, "w") as f:
            json.dump({"cash": self.cash, "positions": self.positions}, f, indent=2)

    def buy(self, ticker: str, shares: int, price: float) -> dict:
        if shares <= 0:
            raise ValueError("Shares must be positive")
        cost = shares * price
        if cost > self.cash:
            raise ValueError(f"Insufficient cash: need ${cost:.2f}, have ${self.cash:.2f}")
        if ticker in self.positions:
            existing = self.positions[ticker]
            total_shares = existing["shares"] + shares
            self.positions[ticker]["avg_cost"] = (
                (existing["shares"] * existing["avg_cost"] + cost) / total_shares
            )
            self.positions[ticker]["shares"] = total_shares
        else:
            self.positions[ticker] = {"shares": shares, "avg_cost": price}
        self.cash -= cost
        self.save()
        return {
            "ticker": ticker, "action": "BUY", "shares": shares,
            "price": price, "total": cost, "timestamp": datetime.now().isoformat()
        }

    def sell(self, ticker: str, shares: int, price: float) -> dict:
        if shares <= 0:
            raise ValueError("Shares must be positive")
        if ticker not in self.positions or self.positions[ticker]["shares"] < shares:
            available = self.positions.get(ticker, {}).get("shares", 0)
            raise ValueError(f"Insufficient shares: need {shares}, have {available}")
        avg_cost = self.positions[ticker]["avg_cost"]
        proceeds = shares * price
        realized_pnl = (price - avg_cost) * shares
        self.positions[ticker]["shares"] -= shares
        if self.positions[ticker]["shares"] == 0:
            del self.positions[ticker]
        self.cash += proceeds
        self.save()
        return {
            "ticker": ticker, "action": "SELL", "shares": shares,
            "price": price, "total": proceeds, "realized_pnl": realized_pnl,
            "timestamp": datetime.now().isoformat()
        }

    def total_value(self, prices: dict) -> float:
        value = self.cash
        for ticker, pos in self.positions.items():
            if ticker in prices:
                value += pos["shares"] * prices[ticker]["price"]
        return value

    def unrealized_pnl(self, prices: dict) -> dict:
        result = {}
        for ticker, pos in self.positions.items():
            if ticker in prices:
                current = prices[ticker]["price"]
                result[ticker] = (current - pos["avg_cost"]) * pos["shares"]
        return result

    def portfolio_summary(self, prices: dict) -> str:
        total = self.total_value(prices)
        lines = [f"Cash: ${self.cash:,.2f}", f"Total Portfolio Value: ${total:,.2f}", ""]
        lines.append(f"{'Ticker':<8} {'Shares':>8} {'Avg Cost':>10} {'Current':>10} {'Mkt Value':>12} {'P&L':>10}")
        lines.append("-" * 60)
        for ticker, pos in self.positions.items():
            price = prices.get(ticker, {}).get("price", 0)
            mkt = pos["shares"] * price
            pnl = (price - pos["avg_cost"]) * pos["shares"]
            lines.append(f"{ticker:<8} {pos['shares']:>8} {pos['avg_cost']:>10.2f} {price:>10.2f} {mkt:>12.2f} {pnl:>10.2f}")
        if not self.positions:
            lines.append("No open positions.")
        return "\n".join(lines)
