import sys
import heapq


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



for _ in range(int(sys.stdin.readline())):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    lines = [[] for __ in range(n + 1)]
    for __ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        lines[a].append([d, b])
        lines[b].append([d, a])
    target = []
    for i in range(t):
        target.append(int(sys.stdin.readline()))
