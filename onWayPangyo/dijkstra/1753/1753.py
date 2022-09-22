import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
import heapq

input = sys.stdin.readline
INF = float("inf")

V, E = map(int, input().split(" "))
K = int(input())
graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split(" "))
    graph[u].append([w, v])
distance = [INF] * (V + 1)


def dijkstra(start):
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


dijkstra(K)
for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])
