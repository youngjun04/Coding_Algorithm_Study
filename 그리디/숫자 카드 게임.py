n, m = map(int, input().split())

max_val = 0

for i in range(n):
    data = list(map(int, input().split()))
    if min(data) > max_val:
        result = min(data)
        max_val = min(data)

print(result)