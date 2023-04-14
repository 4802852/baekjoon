import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline
INF = float("inf")

N, K = map(int, input().split())
coinValue = [int(input()) for _ in range(N)]
dp = [INF] * (K + 1)
dp[0] = 0
for i in coinValue:
    for j in range(i, K + 1):
        if j - i >= 0:
            dp[j] = min(dp[j - i] + 1, dp[j])
print(dp[K] if dp[K] != INF else -1)
