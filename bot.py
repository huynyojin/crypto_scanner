import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(url)
print("Status code:", response.status_code)
print("Raw response:", response.text)
