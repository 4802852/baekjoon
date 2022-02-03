import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from copy import deepcopy

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
ans = []


def move_left(matrix):
    for r in range(N):
        cnt = 0
        now = 0
        for c in range(N):
            if matrix[r][c] == 0:
                continue
            if now == 0:
                now = matrix[r][c]
            else:
                if now == matrix[r][c]:
                    matrix[r][cnt] = 2 * now
                    now = 0
                    cnt += 1
                else:
                    matrix[r][cnt] = now
                    now = matrix[r][c]
                    cnt += 1
            matrix[r][c] = 0
        if now != 0:
            matrix[r][cnt] = now
    return matrix


def move_right(matrix):
    for r in range(N):
        cnt = N - 1
        now = 0
        for c in range(N - 1, -1, -1):
            if matrix[r][c] == 0:
                continue
            if now == 0:
                now = matrix[r][c]
            else:
                if now == matrix[r][c]:
                    matrix[r][cnt] = 2 * now
                    now = 0
                    cnt -= 1
                else:
                    matrix[r][cnt] = now
                    now = matrix[r][c]
                    cnt -= 1
            matrix[r][c] = 0
        if now != 0:
            matrix[r][cnt] = now
    return matrix


def move_up(matrix):
    for c in range(N):
        cnt = 0
        now = 0
        for r in range(N):
            if matrix[r][c] == 0:
                continue
            if now == 0:
                now = matrix[r][c]
            else:
                if now == matrix[r][c]:
                    matrix[cnt][c] = 2 * now
                    now = 0
                    cnt += 1
                else:
                    matrix[cnt][c] = now
                    now = matrix[r][c]
                    cnt += 1
            matrix[r][c] = 0
        if now != 0:
            matrix[cnt][c] = now
    return matrix


def move_down(matrix):
    for c in range(N):
        cnt = N - 1
        now = 0
        for r in range(N - 1, -1, -1):
            if matrix[r][c] == 0:
                continue
            if now == 0:
                now = matrix[r][c]
            else:
                if now == matrix[r][c]:
                    matrix[cnt][c] = 2 * now
                    now = 0
                    cnt -= 1
                else:
                    matrix[cnt][c] = now
                    now = matrix[r][c]
                    cnt -= 1
            matrix[r][c] = 0
        if now != 0:
            matrix[cnt][c] = now
    return matrix


def solve(matrix, depth):
    if depth == 5:
        max_val = 0
        for i in range(N):
            max_val = max(max_val, max(matrix[i]))
        ans.append(max_val)
        return

    solve(move_up(deepcopy(matrix)), depth + 1)
    solve(move_down(deepcopy(matrix)), depth + 1)
    solve(move_left(deepcopy(matrix)), depth + 1)
    solve(move_right(deepcopy(matrix)), depth + 1)


solve(matrix, 0)
print(max(ans))
