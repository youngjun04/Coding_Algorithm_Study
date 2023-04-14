import math

m, n = map(int, input().split())

graph = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if graph[i]:
        j = max(2, m // i)
        while i * j <= n:
            graph[i * j] = False
            j += 1

for i in range(m, n + 1):
    if graph[i]:
        print(i)