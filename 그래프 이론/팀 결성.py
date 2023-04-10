n, m = map(int, input().split())

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

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_parent(parent, b, c)
    elif a == 1:
        if find_parent(parent, b) == find_parent(parent, c):
            print('YES')
        else:
            print('NO')