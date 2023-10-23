import yfinance as yf


def download_prices_long(ticker, period="1mo", interval="60m"):
    data = yf.download(tickers=ticker, period=period, interval=interval)
    # if len(ticker) == 1:
    #     data.columns = [data.columns, pd.Series(tickers * len(data.columns))]
    # data.reset_index(inplace=True)
    # data = data.melt(
    #     id_vars="Datetime", var_name=["Price type", "Instrument"], value_name="Price"
    # )
    print(data)
    print(data.describe())
    pass
