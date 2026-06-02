import argparse

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()


try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    if args.type == "MARKET":

        response = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    else:

        if args.price is None:
            raise ValueError(
                "Price required for LIMIT order"
            )

        validate_price(args.price)

        response = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\n===== ORDER SUMMARY =====")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)

    print("\n===== RESPONSE =====")
    print("Order ID:", response["orderId"])
    print("Status:", response["status"])
    print("Executed Qty:", response["executedQty"])

    print("\nSUCCESS")

except Exception as e:

    print("\nFAILED")
    print(str(e))