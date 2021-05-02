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


n = int(sys.stdin.readline())
parent = [-1 for _ in range(n + 1)]
lines = []
stars = []
for i in range(n):
    a, b = map(float, sys.stdin.readline().split())
    stars.append([a, b])
for i in range(n - 1):
    for j in range(i + 1, n):
        d = distance(stars[i], stars[j])
        heapq.heappush(lines, [d, i, j])
cnt = n - 1
ans = 0
while cnt:
    d, a, b = heapq.heappop(lines)
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        ans += d
        cnt -= 1
print(round(ans, 2))
