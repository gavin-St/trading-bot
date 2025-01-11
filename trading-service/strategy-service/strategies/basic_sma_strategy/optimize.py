def optimize_sma(data, short_range, long_range):
    """
    Optimize SMA strategy using backtest.py.

    Args:
        data (pd.DataFrame): Historical market data for a single ticker.
        short_range (list): Range of short SMA windows to test.
        long_range (list): Range of long SMA windows to test.

    Returns:
        dict: Best short and long SMA window with their performance.
    """
    best_performance = -float('inf')
    best_params = {'short_window': None, 'long_window': None}

    for short_window in short_range:
        for long_window in long_range:
            if short_window >= long_window:
                continue

            signals = sma_strategy(data, short_window, long_window)

            # Use backtest.py or a placeholder for cumulative return
            data['Signal'] = signals.shift(1)
            data['Strategy'] = data['Signal'] * data['Adj Close'].pct_change()
            performance = (1 + data['Strategy']).prod() - 1

            if performance > best_performance:
                best_performance = performance
                best_params['short_window'] = short_window
                best_params['long_window'] = long_window

    return {**best_params, 'performance': best_performance}
