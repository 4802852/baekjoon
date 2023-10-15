import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
forest = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for i in range(0, N):
    tmp = list(map(int, input().split()))
    for j in range(0, N):
        forest[i][j] = tmp[j]
maxVal = 1


def dfs(r, c):
    global maxVal
    if dp[r][c] == 0:
        dp[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue
            if forest[nr][nc] < forest[r][c]:
                dp[r][c] = max(dfs(nr, nc) + 1, dp[r][c])
    maxVal = max(maxVal, dp[r][c])
    return dp[r][c]


for i in range(N):
    for j in range(N):
        dfs(i, j)

print(maxVal)
