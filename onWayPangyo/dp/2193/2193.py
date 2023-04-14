import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
DP = [[0 for _ in range(2)] for __ in range(N + 1)]
DP[1][0] = 0
DP[1][1] = 1
for i in range(2, N + 1):
    DP[i][0] = DP[i - 1][0] + DP[i - 1][1]
    DP[i][1] = DP[i - 1][0]
print(DP[N][0] + DP[N][1])
