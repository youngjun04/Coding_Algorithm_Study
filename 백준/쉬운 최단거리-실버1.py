import sys
import heapq

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

distance = [[INF] * m for _ in range(n)]

def dijkstra(x, y):
    distance[x][y] = 0
    q = []
    heapq.heappush(q,(0, x, y))
    while q:
        dist, x, y = heapq.heappop(q)
        if graph[x][y] == 0 or distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                cost = dist + 1
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            dijkstra(i, j)
            break
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
            continue
        if distance[i][j] == INF:
            print(-1, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()