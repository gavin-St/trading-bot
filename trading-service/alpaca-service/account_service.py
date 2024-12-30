import alpaca_trade_api as tradeapi
from alpaca_service.config import ALPACA_BASE_URL, ALPACA_API_KEY, ALPACA_SECRET_KEY

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL)

def check_account():
    """Fetch account details from Alpaca."""
    return api.get_account()._raw
