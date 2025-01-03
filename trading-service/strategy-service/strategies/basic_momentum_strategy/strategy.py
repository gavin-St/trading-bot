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

start = '2015-01-01'
overall = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
symbols = overall.Symbol.to_list()
print(symbols)

removed = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[1][['Date', 'Removed']]
removed = removed.set_index(removed.Date.Date)
removed.index = pd.to_datetime(removed.index)
removed = removed[removed.index >= start]
removed = removed.Removed.dropna()
print(removed)

symbols.extend(removed.Ticker.to_list())

df = yf.download(symbols, start=start)['Close']
df.index = pd.to_datetime(df.index)

removed[removed.Ticker == ]
