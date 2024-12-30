from alpaca_service.config import api

def get_stock_price(symbol):
    """
    Fetch the latest stock price for a given symbol.

    :param symbol: Stock symbol
    """
    barset = api.get_barset(symbol, 'minute', limit=1)
    return barset[symbol][0].c if symbol in barset else None
