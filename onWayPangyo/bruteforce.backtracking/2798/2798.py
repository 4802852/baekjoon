import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사
N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
visited = [0] * N
result = 0


def dfs(depth, value):
    global result
    if depth == 3:
        if value <= M:
            result = max(result, value)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(depth + 1, value + arr[i])
        visited[i] = 0


dfs(0, 0)
print(result)
