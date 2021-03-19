import sys


n = int(sys.stdin.readline())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    k = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    r = [k, r1, r2]
    r_m = max(r)
    r.remove(r_m)
    if k == 0 and r1 == r2:
        print(-1)
    elif r_m > r[0] + r[1]:
        print(0)
    elif r_m == r[0] + r[1]:
        print(1)
    else:
        print(2)