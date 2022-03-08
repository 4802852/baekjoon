import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

rc = [0, 1, 0, -1]
cc = [1, 0, -1, 0]
R, C, T = map(int, input().split())
matrix = []
conditioner = []
for i in range(R):
    matrix.append(list(map(int, input().split())))
for i in range(R):
    if matrix[i][0] == -1:
        conditioner.append(i)


def circulate(air):
    # 공기 상태 matrix를 입력 받아 써큘레이터가 작동한 후의 공기 상태를 리턴해주는 함수
    n = conditioner[0]
    for i in range(n - 1, 0, -1):
        air[i][0] = air[i - 1][0]
    for i in range(n + 2, R - 1):
        air[i][0] = air[i + 1][0]
    for i in range(C - 1):
        air[0][i] = air[0][i + 1]
        air[R - 1][i] = air[R - 1][i + 1]
    for i in range(0, n):
        air[i][C - 1] = air[i + 1][C - 1]
    for i in range(R - 1, n + 1, -1):
        air[i][C - 1] = air[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        air[n][i] = air[n][i - 1]
        air[n + 1][i] = air[n + 1][i - 1]
    air[n][1] = 0
    air[n + 1][1] = 0
    return air


def diffuse(air):
    # 공기 상태 matrix를 입력 받아, 현재 상태에서 공기가 확산된 후의 공기 상태를 리턴하는 함수
    spread = [[0] * C for _ in range(R)]
    spread[conditioner[0]][0] = -1
    spread[conditioner[1]][0] = -1
    for r in range(R):
        for c in range(C):
            if air[r][c] > 0:
                origin_val = air[r][c]
                spread_val = origin_val // 5
                for i in range(4):
                    nr, nc = r + rc[i], c + cc[i]
                    if 0 <= nr < R and 0 <= nc < C and air[nr][nc] != -1:
                        spread[nr][nc] += spread_val
                        origin_val -= spread_val
                spread[r][c] += origin_val
    return spread


for _ in range(T):
    matrix = diffuse(matrix)
    matrix = circulate(matrix)
total_val = 0
for i in range(R):
    total_val += sum(matrix[i])
print(total_val + 2)
