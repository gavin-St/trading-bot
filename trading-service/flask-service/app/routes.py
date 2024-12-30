from flask import Flask, jsonify, request
from alpaca_service.account_service import check_account
from alpaca_service.order_service import place_order
from alpaca_service.market_data_service import get_stock_price

app = Flask(__name__)

@app.route('/api/account', methods=['GET'])
def get_account():
    account = check_account()
    return jsonify(account)

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    # Replace with actual portfolio fetching logic
    return jsonify({"message": "Portfolio endpoint not implemented yet"})

@app.route('/api/stock_price/<symbol>', methods=['GET'])
def stock_price(symbol):
    price = get_stock_price(symbol)
    return jsonify({"symbol": symbol, "price": price})

@app.route('/api/place_order', methods=['POST'])
def api_place_order():
    data = request.json
    symbol = data.get("symbol")
    qty = data.get("qty")
    side = data.get("side")
    order = place_order(symbol, qty, side)
    return jsonify(order)
