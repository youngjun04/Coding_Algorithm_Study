n = int(input())
k = list(map(int, input().split()))

l = len(k)
d = [0] * l

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, l):
    d[i] = max(d[i - 2] + k[i], d[i - 1])

print(d[l - 1])