import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

rc = [0, -1, 0, 1]
cc = [1, 0, -1, 0]
matrix = [[0] * 101 for _ in range(101)]


def dragon_curve(r, c, d, g):
    curve = [d]
    ng = 0
    matrix[r][c] = 1
    r, c = r + rc[d], c + cc[d]
    matrix[r][c] = 1
    while ng < g:
        for i in range(len(curve) - 1, -1, -1):
            r, c = r + rc[(curve[i] + 1) % 4], c + cc[(curve[i] + 1) % 4]
            curve.append((curve[i] + 1) % 4)
            matrix[r][c] = 1
        ng += 1


N = int(input())
for _ in range(N):
    c, r, d, g = map(int, input().split())
    dragon_curve(r, c, d, g)
cnt = 0
for i in range(len(matrix) - 1):
    for j in range(len(matrix) - 1):
        if (
            matrix[i][j] == 1
            and matrix[i + 1][j] == 1
            and matrix[i][j + 1] == 1
            and matrix[i + 1][j + 1] == 1
        ):
            cnt += 1
print(cnt)
