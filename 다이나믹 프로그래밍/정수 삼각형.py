n = int(input())
tri = [[0] * n for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        tri[i][j] = temp[j]

for i in range(1, n):
    for j in range(n):
        if j == 0:
            left_up = 0
        else:
            left_up = tri[i - 1][j - 1]
        tri[i][j] += max(left_up, tri[i - 1][j])

print(max(tri[n - 1]))