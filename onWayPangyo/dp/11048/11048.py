import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, M = map(int, input().split())
maze = [[0 for _ in range(M + 1)]]
for i in range(N):
    maze.append([0] + list(map(int, input().split())))
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + maze[i][j]

print(dp[-1][-1])
