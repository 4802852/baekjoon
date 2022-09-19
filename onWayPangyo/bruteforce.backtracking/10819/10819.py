import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
arr = list(map(int, input().split(" ")))
visited = [0] * N
result = 0


def dfs(depth, tmp_arr):
    global result
    if depth == N:
        tmp_val = 0
        for i in range(N - 1):
            tmp_val += abs(tmp_arr[i] - tmp_arr[i + 1])
        result = max(result, tmp_val)
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(depth + 1, tmp_arr + [arr[i]])
        visited[i] = 0


dfs(0, [])
print(result)
