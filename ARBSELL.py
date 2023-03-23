import ccxt
import time
import requests

exchange = getattr(ccxt, "bybit")({
    'apiKey': '',
    'secret': '',
    'timeout': 50000,
    'enableRateLimit': True,
    'verbose': True,
    'options': {'adjustForTimeDifference': True,
                'code': 'USDT',  # set default currency exchange-wide
                'marketType': 'linear'
                }})

order_placed = False
while not order_placed:
    try:
        order = exchange.create_order("ARB/USDT", "limit", "sell", "625", 2) #Place Sell order 625 ARB at $2
        order_placed = True
    except ccxt.BaseError as error:
        print(f"An error occurred while placing the order: {error}")
        time.sleep(1) # wait for 1 second before trying again
