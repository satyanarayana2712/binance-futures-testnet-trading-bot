from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    try:
        client = get_client()

        logger.info(
            f"MARKET ORDER REQUEST: "
            f"symbol={symbol}, side={side}, quantity={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET ORDER RESPONSE: {order}")

        return order

    except Exception as e:
        logger.error(f"MARKET ORDER ERROR: {str(e)}")
        raise
def place_limit_order(
    symbol,
    side,
    quantity,
    price
):
    try:
        client = get_client()

        logger.info(
            f"LIMIT ORDER REQUEST: "
            f"symbol={symbol}, side={side}, "
            f"quantity={quantity}, price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(
            f"LIMIT ORDER RESPONSE: {order}"
        )

        return order

    except Exception as e:
        logger.error(
            f"LIMIT ORDER ERROR: {str(e)}"
        )
        raise    