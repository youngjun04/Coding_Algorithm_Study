n = int(input())
num_coin = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    num_coin += n // coin
    n %= coin

print(num_coin)