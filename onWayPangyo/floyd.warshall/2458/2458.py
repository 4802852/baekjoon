import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split(" "))
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

cnt = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] != INF:
            cnt[i] += 1
            cnt[j] += 1
print(cnt.count(N + 1))
