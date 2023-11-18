import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]
prefixSum = [0]
for _ in range(N):
    arr.append(int(input()))
    prefixSum.append(prefixSum[-1] + arr[-1])
dp = [0] * (N + 1)
dp[M] = prefixSum[M]

for i in range(M + 1, N + 1):
    dp[i] = max(dp[i - 1] + arr[i], prefixSum[i] - prefixSum[i - M])

print(max(dp))
