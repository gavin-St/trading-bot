import alpaca_trade_api as tradeapi
from app.utils.config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

# Initialize the Alpaca API client
api = tradeapi.REST(
    key_id=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    base_url=ALPACA_BASE_URL
)

def get_account_details():
    """Fetch account details from Alpaca."""
    return api.get_account()

def fetch_portfolio():
    """Fetch the current portfolio holdings."""
    return api.list_positions()

def get_stock_price(symbol):
    """Fetch the latest stock price for a given symbol."""
    quote = api.get_latest_trade(symbol)
    return quote.price