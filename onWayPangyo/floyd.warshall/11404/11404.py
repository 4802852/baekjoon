import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline
INF = float("inf")

n = int(input())
m = int(input())
arr = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    arr[a][b] = min(arr[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if arr[i][j] == INF else arr[i][j], end=" ")
    print()
