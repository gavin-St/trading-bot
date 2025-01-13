from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

def backtest(strategy, data):
    """
    Backtests a given strategy on the provided data.

    Parameters:
        strategy (Strategy): The trading strategy class to backtest.
        data (pd.DataFrame): The historical data for backtesting. Should contain 'Open', 'High', 'Low', 'Close', and 'Volume' columns.

    Returns:
        list: A list of dictionaries containing the details of each trade (buy/sell) during the backtest.
    """
    bt = Backtest(data, strategy, cash=10_000, commission=0.002)
    results = bt.run()

    bt.plot()

    trades = results['_trades'] 

    trades_list = trades.to_dict('records') if not trades.empty else []
    return trades_list

def optimize(bt):
    optim = bt.optimize(n1 = range(50, 160, 10), n2 = range(50, 160, 10), constraint = lambda x: x.n2 - x.n1 > 20)

    return optim