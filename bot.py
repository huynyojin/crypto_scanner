import requests

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

response = requests.get(url)
data = response.json()

price = data["data"]["amount"]

print(f"BTC Price: {price} USD")
