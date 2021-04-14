import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
lines = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    lines[a].append([c, b])
    lines[b].append([c, a])
f, g = map(int, sys.stdin.readline().split())


def Dijkstara(start, end):
    visited = [float('inf') for _ in range(v + 1)]
    visited[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        weight, now = heapq.heappop(heap)
        if visited[now] < weight:
            continue
        for w, n in lines[now]:
            nw = w + weight
            if nw < visited[n] and nw < visited[end]:
                visited[n] = nw
                heapq.heappush(heap, (nw, n))
    return visited[end]


route11 = Dijkstara(1, f)
route12 = Dijkstara(g, v)
route21 = Dijkstara(1, g)
route22 = Dijkstara(f, v)
ans = min(route11 + route12, route21 + route22) + Dijkstara(f, g)
if ans == float('inf'):
    print(-1)
else:
    print(ans)

