# import heapq
# INF = int(1e9)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))
#     graph[b].append((a, 1))
# x, k = map(int, input().split())


# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))

#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue

#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost, i[0]))

# dijkstra(1)
# a = distance[k]
# distance = [INF] * (n + 1)
# dijkstra(k)

# if distance[x] == INF:
#     print(-1)
# else:
#     print(a + distance[x])

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])