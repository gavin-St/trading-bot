import requests
from alpaca_service.config import alpaca_accounts as accounts
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

def get_accounts():
    """
    Fetch a list of all Alpaca accounts.
    """
    account_details_list = []
    
    for account in accounts:
        # Extract API keys and other account details
        api_key = account["api_key"]
        secret_key = account["secret_key"]

        print(api_key, secret_key)
        
        # Initialize a trading client for each account
        trading_client = TradingClient(api_key, secret_key, paper=True)
        
        # Fetch account details
        account_details = trading_client.get_account()

        # Check if the account is blocked from trading
        if account_details.trading_blocked:
            account_details_list.append({"name": account["name"], "status": "restricted"})
        else:
            account_details_list.append({"name": account["name"], "status": "active", "account_details": account_details})

    return account_details_list

def get_account(account_name):
    """
    Fetch account details from Alpaca for the specified account name.
    """
    print("HIHIHIHIHIHHIHIIHIIHII")
    account_details = next((acc for acc in accounts if acc["name"] == account_name), None)
    if not account_details:
        raise ValueError(f"Account with name '{account_name}' not found.")

    api_key = account_details["api_key"]
    secret_key = account_details["secret_key"]

    print(api_key, secret_key)
    
    trading_client = TradingClient(api_key, secret_key, paper=True)
    
    account = trading_client.get_account()

    if account.trading_blocked:
        print('Account is currently restricted from trading.')
    return account


def get_positions(account_name):
    """
    Fetch all positions from Alpaca for the specified account name.
    """
    account_details = next((acc for acc in accounts if acc["name"] == account_name), None)
    if not account_details:
        raise ValueError(f"Account with name '{account_name}' not found.")
    
    api_key = account_details["api_key"]
    secret_key = account_details["secret_key"]
    
    trading_client = TradingClient(api_key, secret_key, paper=True)
    
    positions = trading_client.get_all_positions()
    
    return positions

def get_portfolio_history(account_name):
    """
    Fetch portfolio history from Alpaca for the specified account name.
    """
    account_details = next((acc for acc in accounts if acc["name"] == account_name), None)
    if not account_details:
        raise ValueError(f"Account with name '{account_name}' not found.")
    
    api_key = account_details["api_key"]
    secret_key = account_details["secret_key"]

    url = "https://paper-api.alpaca.markets/v2/account/portfolio/history?intraday_reporting=market_hours&pnl_reset=per_day"

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": f'{api_key}',
        "APCA-API-SECRET-KEY": f'{secret_key}'
    }

    response = requests.get(url, headers=headers)
    
    return response.json()