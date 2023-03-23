import hashlib
import hmac
import json
import time
import requests

# Replace with your own API key and secret
API_KEY = "YOUR_API_KEY"
API_SECRET = b"YOUR_API_SECRET"

# Set the order details
symbol = "ARBUSDT"
side = "Sell"
price = 2.00
quantity = 625

# Set the API endpoint and parameters
endpoint = "https://api.bybit.com/v2/private/order/create"
params = {
    "api_key": API_KEY,
    "symbol": symbol,
    "side": side,
    "price": price,
    "qty": quantity,
    "time_in_force": "GoodTillCancel",
    "order_type": "Limit",
    "timestamp": int(time.time() * 1000),
}

while True:
    # Create the signature
    params_string = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
    signature = hmac.new(API_SECRET, params_string.encode(), hashlib.sha256).hexdigest()

    # Add the signature to the parameters
    params["sign"] = signature

    # Send the API request
    response = requests.post(endpoint, params=params)
    response_json = response.json()

    # Check if the order was successful
    if response_json["ret_code"] == 0:
        print(f"Order created successfully: {response_json}")
        break  # exit the loop if the order is successful
    else:
        print(f"Order creation failed: {response_json}")
        time.sleep(10)  # wait for 10 seconds before trying again
