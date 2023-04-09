n = int(input())
plans = list(input().split())

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
methods = ['R', 'L', 'U', 'D']

for plan in plans:
    for i in range(len(methods)):
        if methods[i] == plan:
            if x+dx[i] >= 1 and x+dx[i] <= n and y+dy[i] >= 1 and y+dy[i] <= n:
                x += dx[i]
                y += dy[i]
            break

print(x, y)