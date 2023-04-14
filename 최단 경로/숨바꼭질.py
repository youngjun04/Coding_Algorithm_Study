import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n + 1)
distance[1] = 0

q = [(0, 1)]

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

answer = [0, 0, 0]

for i in range(1, n + 1):
    if distance[i] > answer[1]:
        answer[0] = i
        answer[1] = distance[i]

for i in range(1, n + 1):
    if distance[i] == answer[1]:
        answer[2] += 1

for i in range(len(answer)):
    print(answer[i], end=' ')