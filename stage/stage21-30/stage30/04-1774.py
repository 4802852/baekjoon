import sys
import heapq


def distance(x, y):
    return ((x[0] - y[0]) ** 2 + abs(x[1] - y[1]) ** 2) ** 0.5


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


n, m = map(int, sys.stdin.readline().split())
parent = [-1 for _ in range(n + 1)]
lines = []
stars = [[]]
for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    stars.append([a, b])
cnt = n - 1
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ar, br = find(a), find(b)
    if ar != br:
        union(ar, br)
        cnt -= 1
for i in range(1, n):
    for j in range(i + 1, n + 1):
        d = distance(stars[i], stars[j])
        heapq.heappush(lines, [d, i, j])
ans = 0
while cnt:
    d, a, b = heapq.heappop(lines)
    ar, br = find(a), find(b)
    if ar != br:
        union(ar, br)
        ans += d
        cnt -= 1
print("%.2f" % ans)
