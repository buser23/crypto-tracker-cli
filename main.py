import requests

def get_crypto_price(coin_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin_id]['usd']

coins = ["bitcoin", "ethereum", "solana", "cardano"]

print("💹 Crypto Tracker CLI\n----------------------")
for coin in coins:
    price = get_crypto_price(coin)
    print(f"{coin.title():<10}: ${price}")
