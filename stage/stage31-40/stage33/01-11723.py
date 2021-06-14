import sys


s = set()
n = int(sys.stdin.readline())
for _ in range(n):
    i = list(sys.stdin.readline().rstrip().split())
    if len(i) == 1:
        if i[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        c, x = i[0], int(i[1])
        if c == 'add':
            s.add(x)
        elif c == 'remove':
            s.discard(x)
        elif c == 'check':
            print(1 if x in s else 0)
        elif c == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
