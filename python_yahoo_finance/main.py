"""
A script to create a command-line tool using python fire to get stock data from Yahoo Finance
"""

import fire
from lib import get_prices
import time


def main(tickers=["GOOG", "AAPL", "AMZN", "META"], period="1mo", interval="1d"):
    for ticker in tickers:
        start_time = time.time()
        data = get_prices(ticker, period, interval)
        end_time = time.time()
        print(f"Data for {ticker}:")
        print(data)
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        print("=" * 50)


if __name__ == "__main__":
    fire.Fire(main)
