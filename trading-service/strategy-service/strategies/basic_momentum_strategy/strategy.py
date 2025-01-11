import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Fetch historical price data
def fetch_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Step 2: Calculate momentum (e.g., 6-month returns)
def calculate_momentum(prices, lookback_period=126):
    momentum = prices.pct_change(lookback_period)
    return momentum

# Step 3: Rank assets by momentum and select top performers
def rank_assets(momentum_scores, top_n=5):
    ranked = momentum_scores.iloc[-1].sort_values(ascending=False)
    return ranked.head(top_n)

# Step 4: Backtest the strategy
def backtest(prices, top_assets, rebalance_period=20):
    portfolio = pd.DataFrame(index=prices.index)
    portfolio['Portfolio Value'] = 1.0  # Start with $1
    weights = 1 / len(top_assets)  # Equal weighting
    
    for i in range(0, len(prices), rebalance_period):
        selected_assets = prices[top_assets.index].iloc[i:i+rebalance_period]
        returns = selected_assets.pct_change().iloc[1:]  # Daily returns
        portfolio.loc[selected_assets.index, 'Portfolio Value'] *= (1 + (returns * weights).sum(axis=1)).cumprod()
    
    return portfolio

def pricefilter_remove(ticker, df, removed):
    df[ticker] = df[ticker][df[ticker].index <= removed[removed.Ticker == ticker].index[0]]

def pricefilter_add(ticker, df, overall):
    date_added = overall.loc[overall.Symbol == ticker, 'Date added'].iloc[0]
    df[ticker] = df[ticker][df[ticker].index >= date_added]

def momentum(all_mtl_ret, lookback):
    all_mtl_ret_lb = all_mtl_ret.rolling(lookback).agg(lambda x: (x+1).prod() - 1)
    all_mtl_ret_lb.dropna(inplace=True)

    rets = []

    for row in range(len(all_mtl_ret_lb) - 1):
        curr = all_mtl_ret_lb.iloc[row]
        win = curr.nlargest(10)
        win_ret = all_mtl_ret.loc[win.name + MonthEnd(1), win.index]
        rets.append(win_ret.mean())

    return (pd.Series(rets) + 1).prod() - 1

def strategy(market_data, lookback, removed, overall):
    """
    Determines which stock to buy based on momentum strategy.

    Args:
        market_data (pd.DataFrame): Historical market data for multiple tickers.
        lookback (int): Lookback period for momentum calculation (in months).
        removed (pd.DataFrame): DataFrame of tickers removed from the market with their removal dates.
        overall (pd.DataFrame): DataFrame of tickers added to the market with their addition dates.

    Returns:
        str: The ticker symbol of the stock to buy.
    """
    # Apply price filters
    df = market_data.copy()
    for ticker_rem in removed.Ticker:
        if ticker_rem in df.columns:
            pricefilter_remove(ticker_rem, df, removed)

    for ticker_add in overall.Symbol:
        if ticker_add in df.columns:
            pricefilter_add(ticker_add, df, overall)

    # Calculate monthly returns
    monthly_returns = df.pct_change().resample('M').agg(lambda x: (x + 1).prod() - 1)
    twelve_month_returns = monthly_returns.rolling(12).agg(lambda x: (x + 1).prod() - 1)
    twelve_month_returns.dropna(inplace=True)

    # Determine the stock to buy
    latest_returns = twelve_month_returns.iloc[-1]
    top_stock = latest_returns.nlargest(1).index[0]

    return top_stock
