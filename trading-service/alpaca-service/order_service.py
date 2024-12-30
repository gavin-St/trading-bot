from alpaca_service.config import ALPACA_BASE_URL, ALPACA_API_KEY, ALPACA_SECRET_KEY

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL)

def place_order(symbol, qty, side, order_type="market", time_in_force="gtc"):
    """
    Place a buy or sell order via Alpaca API.

    :param symbol: Stock symbol
    :param qty: Quantity
    :param side: 'buy' or 'sell'
    :param order_type: 'market' or 'limit' (default: 'market')
    :param time_in_force: 'day', 'gtc', etc. (default: 'gtc')
    """
    return api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=order_type,
        time_in_force=time_in_force,
    )._raw
