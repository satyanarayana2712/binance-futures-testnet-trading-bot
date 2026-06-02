from bot.orders import place_limit_order

response = place_limit_order(
    symbol="BTCUSDT",
    side="SELL",
    quantity=0.001,
    price=200000
)

print(response)