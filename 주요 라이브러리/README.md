## 내장 함수
- 별도의 import 명령어 없이 사용 가능
### sum()
- iterable 객체의 모든 원소의 합 반환
### min() / max()
- 2개 이상의 파라미터에서 가장 작은/큰 값 반환
### eval()
- 문자열 형식의 수학 수식을 계산한 결과 반환
### sorted()
- iterable 객체에 대해 정렬된 결과 반환
- key 속성으로 정렬 기준 명시 가능
- reverse 속성으로 결과를 뒤집을지 여부 설정 가능

## itertools
- 반복되는 데이터를 처리하는 기능 포함
### permutations
- 순열 계산
- 리스트 자료형으로 변환하여 사용
```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
```
### combinations
- 조합 계산
- 리스트 자료형으로 변환하여 사용
```python
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
```
### product
- 중복 순열 계산
- 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어줌
- 리스트 자료형으로 변환하여 사용
```python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
```
### combinations_with_replacement
- 중복 조합 계산
- 리스트 자료형으로 변환하여 사용
```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
```

## heapq
- 우선순위 큐 기능 구현하고자 할 때 사용
- 파이썬의 힙은 최소 힙으로 구성 - 최상단 원소는 항상 **가장 작은** 원소
- 힙에 원소 삽입할 때는 heapq.heappush(), 원소를 꺼내고자 할 때는 heapq.heappop()
```python
import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
```
- 파이썬에서는 최대 힙 제공하지 않으므로 최대 힙 구현해야 할 때는 원소의 부호를 임시로 변경
```python
import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
```

## bisect
- 이진 탐색 구현 - **정렬된 배열**에서 특정 원소 찾아야 할 때 효과적으로 사용
- bisect_left(a, x) : 정렬된 순서 유지하면서 리스트 a에 데이터 x 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x) : 정렬된 순서 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
- 리스트 [1, 2, 4, 4, 8]이 있을 때 새로운 데이터 4를 삽입하려 한다면 bisec_left(a, 4)와 bisect_right(a, 4)는 각각 인덱스값으로 2와 4를 반환
```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```
- 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구하고자 할 때 효과적으로 사용
```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, -1, 3))
```

## collections
- 유용한 자료구조 제공
### deque
- 큐 구현

||리스트|deque|
|---|---|---|
|가장 앞쪽에 원소 추가|$O(N)$|$O(1)$|
|가장 뒤쪽에 원소 추가|$O(1)$|$O(1)$|
|가장 앞쪽에 원소 제거|$O(N)$|$O(1)$|
|가장 뒤쪽에 원소 제거|$O(1)$|$O(1)$|
- 인덱싱, 슬라이싱 등의 기능은 사용 불가
- 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때 효과적

- 첫 번째 원소 제거 - popleft()
- 마지막 원소 제거 - pop()
- 첫 번째 인덱스에 원소 x 삽입할 때 - appendleft(x)
- 마지막 인덱스에 원소 삽입할 때 - append(x)
- 스택 혹은 큐 자료구조에 모두 사용 가능
    - 큐 자료 구조
        - 원소 삽입 append()
        - 원소 삭제 popleft()
```python
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(list(data))
```
### Counter
- 등장 횟수를 세는 기능 제거 - iterable 객체 내부의 원소가 몇 번씩 등장했는지 알려줌
```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(dict(counter))
```
## math
- 수학적인 기능 포함
- 팩터리얼, 제곱근, 최대공약수 등을 계산해주는 기능 포함
### factorial(x)
- x! 값 반환
```python
import math

print(math.factorial(5))
```
### sqrt(x)
- x의 제곱근 반환
```python
import math

print(math.sqrt(7))
```
### gcd(a, b)
- 최대 공약수 반환
```python
import math

print(math.gcd(21, 14))
```
### pi, e
- 상수 제공
```python
import math

print(math.pi)
print(math.e)
```