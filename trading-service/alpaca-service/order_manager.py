from services.alpaca_service import api

def place_order(symbol, qty, side, order_type="market", time_in_force="gtc"):
    """
    Place an order (buy/sell) on Alpaca.
    
    Args:
        symbol (str): The stock symbol to trade.
        qty (int): Quantity of shares.
        side (str): "buy" or "sell".
        order_type (str): Type of order ("market" or "limit").
        time_in_force (str): Order time validity ("gtc", "day", etc.).

    Returns:
        dict: Order confirmation details.
    """
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=order_type,
        time_in_force=time_in_force
    )
    return {
        "id": order.id,
        "symbol": order.symbol,
        "side": order.side,
        "qty": order.qty,
        "status": order.status
    }

def get_order_status(order_id):
    """Check the status of a specific order."""
    order = api.get_order(order_id)
    return {
        "id": order.id,
        "status": order.status,
        "filled_qty": order.filled_qty
    }
