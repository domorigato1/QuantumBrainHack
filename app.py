import requests
def get_btc_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data = response.json()
    price = data["bitcoin"]["usd"]
    print(f"BTC Price: ${price}")
get_btc_price()
with open("btc_log.txt", "a") as f:
    f.write(f"BTC Price: ${price} at {time.ctime()}\n")