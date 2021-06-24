import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
heap = []
result = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    in_degree[b] += 1
    tree[a].append(b)
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)
while heap:
    now = heapq.heappop(heap)
    result.append(now)
    for i in tree[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(heap, i)
print(*result)
