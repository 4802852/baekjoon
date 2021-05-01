import sys


def find(x):
    if parent[x] < 0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


n, m = map(int, sys.stdin.readline().split())
parent = [-1 for i in range(n + 1)]
for _ in range(m):
    k, a, b = map(int, sys.stdin.readline().split())
    if not k:
        union(a, b)
    if k:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
