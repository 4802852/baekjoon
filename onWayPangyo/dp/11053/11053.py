import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
