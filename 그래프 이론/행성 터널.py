n = int(input())
cities = []
edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    cities.append((i, x, y, z))

for i in range(n):
    a, x, y, z = cities[i]
    for j in range(n):
        if i != j:
            b, nx, ny, nz = cities[j]
            cost = min(abs(x - nx), abs(y - ny), abs(z - nz))
            edges.append((cost, a, b))

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

parent = [i for i in range(n)]

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)