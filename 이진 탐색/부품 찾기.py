n = int(input())
goods = list(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start >= end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

for request in requests:
    if binary_search(goods, request, 0, n - 1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')