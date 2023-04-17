import sys
n = int(sys.stdin.readline())
req = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

def check(cut):
    total = 0
    for i in range(n):
        if req[i] <= cut:
            total += req[i]
        else:
            total += cut
    if total <= m:
        return True
    return False

def binary(start, end):
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            start = mid + 1
        else:
            end = mid - 1
    
    return end

print(binary(1, max(req)))