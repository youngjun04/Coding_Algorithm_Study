# 자료구조
- 데이터를 표현하고 관리하고 처리하기 위한 구조
- 삽입(Push) / 삭제(Pop)

## 스택
- 선입후출 / 후입선출
- 파이썬 기본 리스트 사용
- 삽입 append() / 삭제 pop()

## 큐
- 선입선출
- collections 모듈의 deque 자료구조 활용
- 삽입 append() / 삭제 popleft()

## 재귀 함수
- 자기 자신을 다시 호출하는 함수
- 종료 조건을 명시해야 함
```python
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수 종료')

recursive_function(1)
```
# 그래프
- 노드와 엣지로 표현
- 그래프 탐색 : 하나의 노드를 시작으로 다수의 노드를 방문하는 것
- 프로그래밍에서 그래프는 2가지 방식으로 표현 - 인접 행렬, 인접 리스트
## 인접 행렬 Adjacency Matrix
- 2차원 배열에 각 노드가 연결된 형태 기록
- 연결이 되어 있지 않은 노드끼리는 무한의 비용으로 작성
```python
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
```
## 인접 리스트 Adjacency List
- 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
```python
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))
```
- 메모리 측면에서는 인접 행렬 방식이 비효율적
- 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도는 인접 리스트 방식이 느림

# DFS/BFS
## DFS
- Depth-First Search(깊이 우선 탐색)
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조 이용
- 동작 과정
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리 / 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 2번의 과정을 수행할 수 없을 때까지 반복
- 실제 구현은 재귀 함수를 이용했을 때 매우 간결해짐
```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
```
## BFS
- Breadth First Search(너비 우선 탐색)
- 가까운 노드부터 탐색
- 큐 자료구조 이용
- 동작 과정
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
             if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
```