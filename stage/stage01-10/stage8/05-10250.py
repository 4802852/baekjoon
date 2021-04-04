import sys

n = int(sys.stdin.readline())
for i in range(n):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        rh = h
        rw = n // h
    else:
        rh = n % h
        rw = n // h + 1
    rh = rh * 100
    print(rh + rw)

