import numpy as np

# Features: Moving averages and daily returns
data['SMA_10'] = data['Close'].rolling(window=10).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['RSI'] = 100 - (100 / (1 + data['Return'].rolling(14).mean() / data['Return'].rolling(14).std()))
data.dropna(inplace=True)

# Labels: 1 if next day's close is higher, 0 otherwise
data['Target'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)

# Prepare training and testing datasets
features = ['SMA_10', 'SMA_50', 'RSI']
X = data[features]
y = data['Target']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def sma_strategy(data, short_window, long_window):
    """
    Simple SMA strategy to determine buy/sell signals.

    Args:
        data (pd.DataFrame): Historical market data for a single ticker (e.g., Adj Close prices).
        short_window (int): Lookback period for the short SMA.
        long_window (int): Lookback period for the long SMA.

    Returns:
        pd.Series: Buy (1) and sell (-1) signals.
    """
    data = data.copy()
    data['SMA_short'] = data['Adj Close'].rolling(window=short_window).mean()
    data['SMA_long'] = data['Adj Close'].rolling(window=long_window).mean()
    data['Signal'] = 0
    data.loc[data['SMA_short'] > data['SMA_long'], 'Signal'] = 1
    data.loc[data['SMA_short'] <= data['SMA_long'], 'Signal'] = -1
    return data['Signal']