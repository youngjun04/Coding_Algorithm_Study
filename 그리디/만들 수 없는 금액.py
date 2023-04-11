from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))

sums = []

for i in range(1, len(coins) + 1):
    combs = list(combinations(coins, i))
    for comb in combs:
        sums.append(sum(comb))

for i in range(1, max(sums) + 2):
    if i not in sums:
        print(i)
        break