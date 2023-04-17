import sys

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    edges.append(list(map(int, sys.stdin.readline().split())))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n + 1)]

for edge in edges:
    a, b = edge
    union_parent(parent, a, b)

for i in range(1, n + 1):
    parent[i] = find_parent(parent, parent[i])

result = []
for i in range(1, n + 1):
    if parent[i] not in result:
        result.append(parent[i])

print(len(result))