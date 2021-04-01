import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    q = deque(p)
    bb = deque([0 for _ in range(a)])
    bb[b] = 1
    bbq = []
    while len(q) > 0:
        maximum = max(q)
        while q[0] != maximum:
            q.append(q.popleft())
            bb.append(bb.popleft())
        q.popleft()
        bbq.append(bb.popleft())
    print(bbq.index(1) + 1)
