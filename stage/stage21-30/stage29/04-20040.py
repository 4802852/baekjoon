import sys


def find(x):
    if connect[x] == x:
        return x
    p = find(connect[x])
    connect[x] = p
    return p


def union(x, y):
    connect[y] = x


sys.setrecursionlimit(10 ** 9)
n, m = map(int, sys.stdin.readline().split())
connect = [i for i in range(n)]
i = 0
ans = 0
while i != m:
    a, b = map(int, sys.stdin.readline().split())
    ar = find(a)
    br = find(b)
    if ar == br:
        ans = i + 1
        break
    else:
        union(ar, br)
    i += 1
print(ans)
