import sys
m = int(sys.stdin.readline())

ops = []
for _ in range(m):
    ops.append(list(sys.stdin.readline().split()))

S = set()
for op in ops:
    if len(op) == 1:
        if op[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        a, b = op
        if a == 'add':
            S = S | set([int(b)])
        elif a == 'remove':
            S -= set([int(b)])
        elif a == 'check':
            if int(b) in S:
                print(1)
            else:
                print(0)
        elif a == 'toggle':
            if int(b) in S:
                S -= set([int(b)])
            else:
                S = S | set([int(b)])