import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(url)
data = response.json()

print("Full JSON:", data)

if "price" in data:
    price = data["price"]
    print(f"🔥 BTC Price: {price} USDT")
else:
    print("Unexpected response format")
