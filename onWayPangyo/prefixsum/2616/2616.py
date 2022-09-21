import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

N = int(input())
train = list(map(int, input().split(" ")))
L = int(input())
ans = 0

sum_train = [0] * (N + 1)
for i in range(1, N + 1):
    sum_train[i] = sum_train[i - 1] + train[i - 1]
dp = [[0] * (4) for _ in range(N + 1)]

for j in range(1, 4):
    for i in range(1, N + 1):
        if i - L * j < 0 or N + 1 - L * (3 - j) <= i:
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i - L][j - 1] + sum_train[i] - sum_train[i - L])

print(dp[-1][-1])
