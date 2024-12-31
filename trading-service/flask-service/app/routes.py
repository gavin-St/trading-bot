import json
from flask import Blueprint, jsonify, request
from alpaca_service.account_service import get_accounts, get_account, get_positions, get_portfolio_history
from alpaca_service.order_service import place_order
# from alpaca_service.market_data_service import get_stock_price

bp = Blueprint('api_routes', __name__)

@bp.route('/api/accounts', methods=['GET'])
def api_get_accounts():
    """
    Get a list of all accounts.
    """
    account = get_accounts()
    accounts_list = [account.__dict__ for account in accounts]
    return jsonify(accounts_list)

@bp.route('/api/accounts/<account_name>', methods=['GET'])
def api_get_account(account_name):
    """
    Get details for a specific account by name.
    """
    account = get_account(account_name) 
    account_data = account.__dict__
    return jsonify(account_data)

@bp.route('/api/accounts/<account_name>/positions', methods=['GET'])
def api_get_positions(account_name):
    """
    Get portfolio positions for a specific account.
    """
    positions = get_positions(account_name) 
    positions_list = [item.__dict__ for item in positions]
    return jsonify(positions_list)

@bp.route('/api/accounts/<account_name>/history', methods=['GET'])
def api_get_portfolio_history(account_name):
    """
    Get portfolio history for a specific account.
    """
    history = get_portfolio_history(account_name)
    return jsonify(history)

@bp.route('/api/accounts/<account_name>/place_order', methods=['POST'])
def api_place_order(account_name):
    """
    Place an order for a specific account.
    """
    # Extract order details from the request body.
    order_data = request.get_json()
    
    # Pass account_name and order_data to the place_order function.
    order = place_order(account_name, **order_data)
    return jsonify(order)

# @bp.route('/api/stock_price/<symbol>', methods=['GET'])
# def stock_price(symbol):
#     price = get_stock_price(symbol)
#     return jsonify({"symbol": symbol, "price": price})
