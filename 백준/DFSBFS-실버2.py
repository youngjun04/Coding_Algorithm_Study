from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

d = []
b = []

visited = [False] * (n + 1)
def dfs(start):
    visited[start] = True
    d.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
def bfs(start):
    visited[start] = True
    b.append(start)
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                b.append(i)
                q.append(i)
                visited[i] = True

dfs(v)
for i in range(n + 1):
    visited[i] = False
bfs(v)

for m in d:
    print(m, end=' ')
print()
for n in b:
    print(n, end=' ')