"""
A script to create a command-line tool using python fire to get stock data from Yahoo Finance
"""

import fire
from lib import get_prices
import time


def main(ticker="AAPL", period="1mo", interval="1d"):
    start_time = time.time()
    data = get_prices(ticker, period, interval)
    print(data)
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time}")
    pass


if __name__ == "__main__":
    fire.Fire(main)
