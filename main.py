from crypto_data import get_coins, Coin
import time

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!TRIGGERED!!!')
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    while True:
        time.sleep(5)
        alert('btc', bottom=20_000, top=60_000, coins_list=coins)
        alert('eth', bottom=1800, top=1900, coins_list=coins)
        alert('xrp', bottom=0.47, top=0.48, coins_list=coins)
