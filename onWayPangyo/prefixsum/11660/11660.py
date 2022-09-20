import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

N, M = map(int, sys.stdin.readline().split(" "))
arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0] + list(map(int, sys.stdin.readline().split(" "))))
sum_arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    tmp_sum = 0
    for j in range(1, N + 1):
        tmp_sum += arr[i][j]
        sum_arr[i][j] = tmp_sum + sum_arr[i - 1][j]


def prefixSum(x1, y1, x2, y2):
    return sum_arr[x2][y2] - sum_arr[x1 - 1][y2] - sum_arr[x2][y1 - 1] + sum_arr[x1 - 1][y1 - 1]


for t in range(M):
    print(prefixSum(*map(int, sys.stdin.readline().split(" "))))
