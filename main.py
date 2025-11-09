#!/usr/bin/env python3
import requests

def get_crypto_price(coin_id="bitcoin"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": coin_id, "vs_currencies": "usd"}
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # levanta erro se o request falhar
        data = response.json()
        return data.get(coin_id, {}).get("usd", "N/A")
    except Exception as e:
        print(f"⚠️ Error fetching {coin_id}: {e}")
        return "Error"

def main():
    coins = ["bitcoin", "ethereum", "solana", "cardano"]
    print("💹 Crypto Tracker CLI\n----------------------")

    for coin in coins:
        price = get_crypto_price(coin)
        print(f"{coin.title():<10}: ${price}")

if __name__ == "__main__":
    main()
