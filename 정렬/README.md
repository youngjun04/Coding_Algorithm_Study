# 정렬
- 데이터를 특정한 기준에 따라서 순서대로 나열
## 선택 정렬
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
```
- 시간 복잡도 $O(N^2)$
## 삽입 정렬
- 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입
- 필요할 때만 위치를 바꾸므로 데이터가 거의 정렬되어 있을 때 효율적
- 특정한 데이터가 적절한 위치에 들어가기 이전에 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
```
- 시간 복잡도 $O(N^2)$
## 퀵 정렬
- 기준을 설정한 다음 기준보다 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
```
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
- 시간 복잡도 $O(NlogN)$
## 계수 정렬
- 모든 범위를 담을 수 있는 크기의 리스트 선언하고 그 안에 정렬에 대한 정보를 담음
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(len(count[i])):
        print(i, end=' ')
```
- 시간 복잡도 $O(N+K)$ (데이터 개수 N, 최대값 크기 K)
## 파이썬 정렬 라이브러리
- sorted()
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
```
- sort() : 내부 원소 바로 정렬
- key 매개변수를 입력으로 받아 정렬 기준이 됨
- 시간 복잡도 $O(NlogN)$