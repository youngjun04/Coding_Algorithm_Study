n, x = map(int, input().split())
numbers = list(map(int, input().split()))

def left_search(array, answer, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == answer and (array[mid - 1] < answer or mid == 0):
        return mid
    else:
        if array[mid] < answer:
            return left_search(array, answer, mid + 1, end)
        elif array[mid] >= answer:
            return left_search(array, answer, start, mid - 1)

def right_search(array, answer, start, end):
    mid = (start + end) // 2
    if array[mid] == answer and (array[mid + 1] > answer or mid == n - 1):
        return mid
    else:
        if array[mid] <= answer:
            return right_search(array, answer, mid + 1, end)
        elif array[mid] > answer:
            return right_search(array, answer, start, mid - 1)

def count_by_value(array, x):

    n = len(array)
    a = left_search(array, x, 0, n - 1)
    if a == None:
        return 0

    b = right_search(array, x, 0, n - 1)

    return b - a + 1

count = count_by_value(numbers, x)

if count == 0:
    print(-1)
else:
    print(count)