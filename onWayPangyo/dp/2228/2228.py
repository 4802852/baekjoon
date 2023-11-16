import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
concluded = [[0] + [float("-inf")] * M for _ in range(N + 1)]
notConcluded = [[0] + [float("-inf")] * M for _ in range(N + 1)]

for i in range(1, N + 1):
    num = int(input())
    for j in range(1, M + 1):
        notConcluded[i][j] = max(concluded[i - 1][j], notConcluded[i - 1][j])
        concluded[i][j] = max(concluded[i - 1][j], notConcluded[i - 1][j - 1]) + num

print(max(concluded[N][M], notConcluded[N][M]))
