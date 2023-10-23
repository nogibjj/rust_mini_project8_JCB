"""
A script to create a command-line tool using python fire to get stock data from Yahoo Finance
"""

import fire
from lib import get_prices


def main(ticker="AAPL", period="1mo", interval="1d"):
    data = get_prices(ticker, period, interval)
    print(data)
    pass


if __name__ == "__main__":
    fire.Fire(main)
