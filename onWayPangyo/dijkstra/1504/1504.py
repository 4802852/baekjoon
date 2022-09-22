import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
import heapq

input = sys.stdin.readline
INF = float("inf")

N, E = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split(" "))
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split(" "))


def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    pq = [(0, start)]
    while pq:
        weight, now = heapq.heappop(pq)
        if distance[now] < weight:
            continue
        for w, n in graph[now]:
            nw = w + weight
            if nw < distance[n]:
                distance[n] = nw
                heapq.heappush(pq, (nw, n))
    return distance


dv1 = dijkstra(v1)
dv2 = dijkstra(v2)
mind = min(dv1[1] + dv1[v2] + dv2[N], dv1[N] + dv1[v2] + dv2[1])
print(-1 if mind == INF else mind)
