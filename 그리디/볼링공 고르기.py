from itertools import combinations

n, m = map(int, input().split())
weights = list(map(int, input().split()))
count = 0

methods = list(combinations(weights, 2))
for method in methods:
    a, b = method
    if a != b:
        count += 1

print(count)