import sys
import heapq


def Dijkstara(start):
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
            if nw < visited[n]:
                visited[n] = nw
                heapq.heappush(heap, (nw, n))
    return visited


for _ in range(int(sys.stdin.readline())):
    v, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    lines = [[] for __ in range(v + 1)]
    for __ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        if (a == g and b == h) or (a == h and b == g):
            lines[a].append([d - 0.1, b])
            lines[b].append([d - 0.1, a])
        else:
            lines[a].append([d, b])
            lines[b].append([d, a])
    target = []
    for i in range(t):
        target.append(int(sys.stdin.readline()))
    ans = []
    sr = Dijkstara(s)
    for tar in target:
        if sr[tar] != float('inf') and type(sr[tar]) == float:
            ans.append(tar)
    ans.sort()
    print(*ans)