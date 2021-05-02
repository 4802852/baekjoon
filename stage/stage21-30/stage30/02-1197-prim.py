import sys
import heapq


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


v, e = map(int, sys.stdin.readline().split())
parent = [-1 for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
cnt = v - 1
tmp = graph[1][::]
heapq.heapify(tmp)
ans = 0
a = 1
while cnt:
    d, n = heapq.heappop(tmp)
    ar, nr = find(a), find(n)
    if ar != nr:
        union(ar, nr)
        ans += d
        for i in graph[n]:
            heapq.heappush(tmp, i)
        cnt -= 1
print(ans)
