import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
from collections import defaultdict

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
arr = defaultdict(list)
forest = [[0] * (N + 2) for _ in range(N + 2)]
dp = [[0] * (N + 2) for _ in range(N + 2)]
for i in range(1, N + 1):
    tmp = [0] + list(map(int, input().split()))
    for j in range(1, N + 1):
        forest[i][j] = tmp[j]
        arr[tmp[j]].append((i, j))
        dp[i][j] = 1
maxVal = 1

for tree in sorted(arr.keys()):
    tmp_arr = arr[tree]
    while tmp_arr:
        r, c = tmp_arr.pop()
        for i in range(4):
            if forest[r + dr[i]][c + dc[i]] < forest[r][c]:
                dp[r][c] = max(dp[r + dr[i]][c + dc[i]] + 1, dp[r][c])
                maxVal = max(maxVal, dp[r][c])

print(maxVal)
