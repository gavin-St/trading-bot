import yfinance as yf
import pandas as pd

def get_market_data(ticker, start_date, end_date, interval="1d"):
    """
    Fetches historical market data for a specific security using yfinance.

    Args:
        ticker (str): The ticker symbol of the security (e.g., 'AAPL', 'GOOGL').
        start_date (str): The start date for fetching data (format: 'YYYY-MM-DD').
        end_date (str): The end date for fetching data (format: 'YYYY-MM-DD').
        interval (str): The interval for the data (default is '1d'). Possible values: ['1m', '5m', '15m', '1d', '1wk', '1mo'].

    Returns:
        pd.DataFrame: A DataFrame containing the historical market data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker} in the specified date range.")
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame()

def get_sp500_data(start_date, end_date, interval="1d"):
    """
    Fetches historical market data for the S&P 500 index.

    Args:
        start_date (str): The start date for fetching data (format: 'YYYY-MM-DD').
        end_date (str): The end date for fetching data (format: 'YYYY-MM-DD').
        interval (str): The interval for the data (default is '1d'). Possible values: ['1m', '5m', '15m', '1d', '1wk', '1mo'].

    Returns:
        pd.DataFrame: A DataFrame containing the historical market data for the S&P 500 index.
    """
    sp500_ticker = "^GSPC"
    return get_market_data(sp500_ticker, start_date, end_date, interval)