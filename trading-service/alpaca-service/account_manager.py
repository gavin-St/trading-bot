from services.alpaca_service import get_account_details, fetch_portfolio

def check_account():
    """Check the account details like balance, buying power, etc."""
    account = get_account_details()
    return {
        "balance": account.cash,
        "buying_power": account.buying_power,
        "status": account.status
    }

def get_portfolio():
    """Get the portfolio's current holdings."""
    portfolio = fetch_portfolio()
    return [
        {
            "symbol": position.symbol,
            "quantity": position.qty,
            "market_value": position.market_value
        }
        for position in portfolio
    ]
