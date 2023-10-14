import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

m = [""] + list(map(str, input().strip()))
n = [""] + list(map(str, input().strip()))
dp = [[0] * 1002 for _ in range(1002)]

for i in range(1, len(m)):
    for j in range(1, len(n)):
        if m[i] == n[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(m) - 1][len(n) - 1])
