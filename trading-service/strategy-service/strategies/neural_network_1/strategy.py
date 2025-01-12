import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

def strategy(data, model_path):
    """
    Neural Network strategy to generate buy/sell signals.

    Args:
        data (pd.DataFrame): Historical market data (including 'Adj Close').
        model_path (str): Path to the pre-trained neural network model.

    Returns:
        pd.Series: Predicted buy (1) and sell (-1) signals.
    """
    data = data.copy()

    # Load the trained model
    model = tf.keras.models.load_model(model_path)

    # Prepare features for prediction
    features = data[['Adj Close']].pct_change().dropna().values
    features = StandardScaler().fit_transform(features)

    # Generate predictions
    predictions = model.predict(features)
    data = data.iloc[1:]  # Align with predictions
    data['Signal'] = np.where(predictions.flatten() > 0.5, 1, -1)

    return data['Signal']