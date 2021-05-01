import sys


def find(x):
    if connect[x] < 0:
        return x
    p = find(connect[x])
    connect[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if connect[x] < connect[y]:
        connect[x] += connect[y]
        connect[y] = x
    else:
        connect[y] += connect[x]
        connect[x] = y


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
connect = [-1 for i in range(n + 1)]
for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    for j in range(len(k)):
        if k[j]:
            union(i + 1, j + 1)
p = list(map(int, sys.stdin.readline().split()))
q = find(p[0])
isPossible = True
for i in p:
    if q != find(i):
        isPossible = False
if isPossible:
    print('YES')
else:
    print('NO')