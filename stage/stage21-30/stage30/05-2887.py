import sys


def find(x):
    if parent[x] < 0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


n = int(sys.stdin.readline())
parent = [-1 for _ in range(n + 1)]
lines = []
stars = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    stars.append([a, b, c, i])
for j in range(3):
    stars.sort(key=lambda x: x[j])
    before = stars[0][3]
    for i in range(1, n):
        current = stars[i][3]
        lines.append([abs(stars[i][j] - stars[i - 1][j]), before, current])
        before = current
lines.sort(key=lambda x: x[0])
cnt = n - 1
ans = 0
while cnt:
    d, a, b = lines.pop(0)
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        ans += d
        cnt -= 1
print(ans)
