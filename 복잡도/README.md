# 복잡도
- **시간복잡도**
    - 특정한 크기의 입력에 대해 알고리즘이 얼마나 오래 걸리는지
    - 알고리즘을 위해 필요한 연산의 횟수
- **공간복잡도**    
    - 특정한 크기의 입력에 대해 알고리즘이 얼마나 많은 메모리를 차지하는지
    - 알고리즘을 위해 필요한 메모리의 양

## 시간복잡도
- 빅오(Big-O) 표기법 사용 : 가장 빠르게 증가하는 항만을 고려
```python
array = [3, 5, 1, 2, 4]
summary = 0

for x in array:
    summary += x

print(summary)
```
- 이 경우 반복문 부분이 가장 큰 영향력 - 시간복잡도 $O(N)$
```python
a = 5
b = 7
print(a + b)
```
- 상수 연산 - 시간복잡도 $O(1)$
```python
array = [3, 5, 1, 2, 4]

for i in array:
    for j in array:
        temp = i + j
        print(temp)
```
- 2중 반복문 - 시간복잡도 $O(N^2)$

|빅오 표기법|명칭|
|---|---|
|$O(1)$|상수 시간(Constant time)|
|$O(logN)$|로그 시간(Log time)|
|$O(N)$|선형 시간|
|$O(NlogN)$|로그 선형 시간|
|$O(N^2)$|이차 시간|
|$O(N^3)$|삼차 시간|
|$O(2^n)$|지수 시간|

||N이 1,000일 때의 연산 횟수|
|---|---|
|$O(N)$|1,000|
|$O(NlogN)$|10,000|
|$O(N^2)$|1,000,000|
|$O(N^3)$|1,000,000,000|

- 일반적으로 연산 횟수가 10억 넘어가면 C 언어 기준 1초 이상의 시간 - 오답 판정

예시
- N의 범위가 500 : $O(N^3)$ 알고리즘 설계
- N의 범위가 2,000 : $O(N^2)$ 알고리즘 설계
- N의 범위가 100,000 : $O(NlogN)$ 알고리즘 설계
- N의 범위가 10,000,000 : $O(N)$ 알고리즘 설계

- 연산 횟수 1억 이하로 설계하기!

## 공간복잡도
- 시간복잡도와 마찬가지로 빅오 표기법 이용
- int를 기준으로 리스트 크기에 따른 메모리 사용량
    - int a[1000] : 4kB
    - int a[1000000] : 4MB
    - int a[2000][2000] : 16MB
- 보통 코딩 테스트 메모리 제한 128 ~ 512 MB 정도 - 데이터 개수 1,000만 단위 넘지 않도록 설계

## 시간 측정
```python
import time
start_time = time.time()

end_time = time.time()
print('time : ', end_time - start_time)
```

**선택 정렬, 기본 정렬 라이브러리 수행시간 비교**
```python
from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 선택 정렬
start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print('선택 정렬 시간 : ', end_time - start_time)

array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 기본 정렬 라이브러리
start_time = time.time()

array.sort()

end_time = time.time()
print('기본 정렬 라이브러리 시간 : ', end_time - start_time)