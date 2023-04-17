import sys
h, w, n, m = map(int, sys.stdin.readline().split())

row = w // (m + 1) if w % (m + 1) == 0 else w // (m + 1) + 1
col = h // (n + 1) if h % (n + 1) == 0 else h // (n + 1) + 1

print(row * col)