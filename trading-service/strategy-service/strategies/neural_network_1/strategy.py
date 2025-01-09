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
