# 서로소 집합
- 공통 원소가 없는 두 집합
## 서로소 집합 자료구조
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- union과 find 2개의 연산으로 조작
    - union : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
    - find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
- 트리 자료구조 이용하여 집합 표현
- 알고리즘
1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
    - A와 B의 루트 노드 A', B'를 각각 찾음
    - A'를 B'의 부모 노드로 설정 (B'가 A'를 가리키도록 함)
2. 모든 union 연산을 처리할 때까지 1번 과정 반복
```python
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```
- 경로 압축 기법으로 시간 복잡도 개선 가능
    - find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```
## 서로소 집합을 활용한 사이클 판별
- 무방향 그래프 내에서의 사이클 판별할 때 사용 가능
- 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정 반복
    1. 각 간선을 확인하며 두 노드의 루트 노드 확인
        - 루트 노드가 서로 다르다면 두 노드에 대해 union 연산 수행
        - 루트 노드가 서로 같다면 사이클 발생
    2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정 반복
- 모든 간선을 하나씩 확인, 매 간선에 대해 union 및 find 함수 호출하는 방식으로 동작
```python
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
        parnet[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 발생 X')
```
# 신장 트리
- 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
## 크루스칼 알고리즘
- 최소 신장 트리 알고리즘 : 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘
- 가장 적은 비용으로 모든 노드 연결 가능
- 모든 간선에 대해 정렬 수행한 뒤 가장 거리가 짧은 간선부터 집합에 포함시킴
    - 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않음
1. 간선 데이터를 비용에 따라 오름차순 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클 발생시키는지 확인
    - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
    - 사이클이 발생하는 경우 포함 X
3. 모든 간선에 대해 2번 과정 반복
- 최종적으로 신장 트리에 포함되는 간선의 개수 = 노드의 개수 - 1
```python
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

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```
- 시간 복잡도 $O(ElogE)$

# 위상 정렬
- 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
- 진입 차수 : 특정한 노드로 '들어오는' 간선의 개수
1. 진입차수가 0인 노드를 큐에 넣음
2. 큐가 빌 때까지 다음 과정 반복
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣음
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클 존재한다고 판단
```python
from collections import deque
v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()
```
- 시간 복잡도 $O(V+E)$
