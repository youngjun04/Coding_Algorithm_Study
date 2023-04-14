g = int(input())
p = int(input())

array = []

for _ in range(p):
    array.append(int(input()))

parent = [i for i in range(g + 1)]

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
result = 0
for plane in array:
    x = find_parent(parent, plane)
    if x == 0:
        break
    else:
        union_parent(parent, x, x - 1)
        result += 1

print(result)