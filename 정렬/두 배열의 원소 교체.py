n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(k):
    a.sort()
    b.sort()
    if a[0] <= b[n - 1]:
        a[0], b[n - 1] = b[n - 1], a[0]
    else:
        break
        

print(sum(a))