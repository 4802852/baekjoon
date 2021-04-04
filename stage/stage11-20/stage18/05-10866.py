import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque([])
for i in range(n):
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == 'push_front':
        dq.appendleft(a[1])
    elif a[0] == 'push_back':
        dq.append(a[1])
    elif a[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(dq))
    elif a[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
