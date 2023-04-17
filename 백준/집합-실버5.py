import sys
m = int(sys.stdin.readline())

S = set()
for _ in range(m):
    op = sys.stdin.readline().split()

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