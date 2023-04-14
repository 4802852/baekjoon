import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coinValue = [int(input()) for _ in range(N)]
dp = [0] * (K + 1)
dp[0] = 1
for i in coinValue:
    for j in range(i, K + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[K])
