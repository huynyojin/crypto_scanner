import requests

def get_btc_price():
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response = requests.get(url)
    data = response.json()

    price = data["data"]["amount"]
    return price

if __name__ == "__main__":
    price = get_btc_price()
    print(f"🔥 BTC price: {price} USD")
