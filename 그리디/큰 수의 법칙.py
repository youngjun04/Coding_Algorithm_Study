n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

x = m // (k + 1)
y = m % (k + 1)

result = (data[n - 1] * k + data[n - 2]) * x + data[n - 1] * y

print(result)