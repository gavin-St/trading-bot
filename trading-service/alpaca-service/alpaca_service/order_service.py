import json
from alpaca_service.config import alpaca_accounts as accounts
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

def place_order(account_name, order_data):
    """
    Intermediate function to process and place an order from an order_data dictionary.
    
    :param order_data: A dictionary containing the order details.
                       Expected keys: account_name, symbol, qty, side, time_in_force
    :return: The submitted order details.
    """
    # Get Account
    
    account_details = next((acc for acc in accounts if acc["name"] == account_name), None)
    
    if not account_details:
        raise ValueError(f"Account with name '{account_name}' not found.")
    
    api_key = account_details["api_key"]
    secret_key = account_details["secret_key"]
    
    trading_client = TradingClient(api_key, secret_key, paper=True)

    # Extract fields from the order_data object.
    symbol = order_data.get("symbol")
    qty = order_data.get("qty")
    side = order_data.get("side")
    type = order_data.get("type")
    time_in_force = order_data.get("time_in_force", "gtc")
    limit_price = order_data.get("limit_price")
    stop_price = order_data.get("stop_price")
    trail_price = order_data.get("trail_price")
    trail_percent = order_data.get("trail_percent")
    extended_hours = order_data.get("extended_hours", False)
    client_order_id = order_data.get("client_order_id")
    order_class = order_data.get("order_class", "")
    bracket = order_data.get("bracket")
    take_profit = order_data.get("take_profit")
    stop_loss = order_data.get("stop_loss")
    position_intent = order_data.get("position_intent")

    # Validate required fields
    if not symbol or not qty or not side or not type:
        raise ValueError("Missing required fields in order_data.")

    # Create the order request based on the type
    if type.lower() == "market":
        # Market order
        market_order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide(side.lower()),
            time_in_force=TimeInForce(time_in_force.upper())
        )
        return trading_client.submit_order(order_data=market_order_data)

    elif type.lower() == "limit":
        # Limit order - need limit_price
        if not limit_price:
            raise ValueError("limit_price is required for limit orders.")
        
        limit_order_data = LimitOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide(side.lower()),
            limit_price=limit_price,
            time_in_force=TimeInForce(time_in_force.upper())
        )
        return trading_client.submit_order(order_data=limit_order_data)

    elif type.lower() == "stop_limit":
        # Stop limit order - need stop_price and limit_price
        if not stop_price or not limit_price:
            raise ValueError("stop_price and limit_price are required for stop_limit orders.")
        
        stop_limit_order_data = StopLimitOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide(side.lower()),
            stop_price=stop_price,
            limit_price=limit_price,
            time_in_force=TimeInForce(time_in_force.upper())
        )
        return trading_client.submit_order(order_data=stop_limit_order_data)

    elif type.lower() == "trailing_stop":
        # Trailing stop order - need either trail_price or trail_percent
        if not trail_price and not trail_percent:
            raise ValueError("Either trail_price or trail_percent is required for trailing_stop orders.")
        
        trailing_stop_order_data = TrailingStopOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide(side.lower()),
            trail_price=trail_price,
            trail_percent=trail_percent,
            time_in_force=TimeInForce(time_in_force.upper())
        )
        return trading_client.submit_order(order_data=trailing_stop_order_data)

    else:
        raise ValueError("Unsupported order type.")



# # preparing limit order
# limit_order_data = LimitOrderRequest(
#                     symbol="BTC/USD",
#                     limit_price=17000,
#                     notional=4000,
#                     side=OrderSide.SELL,
#                     time_in_force=TimeInForce.FOK
#                    )

# # Limit order
# limit_order = trading_client.submit_order(
#                 order_data=limit_order_data
#               )
