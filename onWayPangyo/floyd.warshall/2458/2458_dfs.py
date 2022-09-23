import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split(" "))
taller_graph = [[] for _ in range(N + 1)]
shorter_graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    taller_graph[a].append(b)
    shorter_graph[b].append(a)
taller = [set() for _ in range(N + 1)]
shorter = [set() for _ in range(N + 1)]
taller_num = [0] * (N + 1)
shorter_num = [0] * (N + 1)


def find_taller(i):
    if taller_num[i]:
        return taller[i]
    taller_num[i] = 1
    for j in taller_graph[i]:
        taller[i].add(j)
        taller[i] |= find_taller(j)
    return taller[i]


def find_shorter(i):
    if shorter_num[i]:
        return shorter[i]
    shorter_num[i] = 1
    for j in shorter_graph[i]:
        shorter[i].add(j)
        shorter[i] |= find_shorter(j)
    return shorter[i]


cnt = 0
for i in range(1, N + 1):
    find_taller(i)
    find_shorter(i)
    if len(taller[i]) + len(shorter[i]) == N - 1:
        cnt += 1
print(cnt)
