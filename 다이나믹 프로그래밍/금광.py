t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    golds = [[0] * m for _ in range(n)]
    nums = list(map(int, input().split()))
    k = 0
    for i in range(n):
        for j in range(m):
            golds[i][j] = nums[k]
            k += 1

    d = [[0] * m for _ in range(n)]

    for i in range(n):
        d[i][0] = golds[i][0]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                d[i][j] = golds[i][j] + max(d[i][j - 1], d[i + 1][j - 1])
            elif i == n - 1:
                d[i][j] = golds[i][j] + max(d[i][j - 1], d[i - 1][j - 1])
            else:
                d[i][j] = golds[i][j] + max(d[i][j - 1], d[i - 1][j - 1], d[i + 1][j - 1])
    
    max_val = 0
    for i in range(n):
        max_val = max(max_val, d[i][m -1])
    print(max_val)