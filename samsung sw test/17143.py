import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from copy import deepcopy

R, C, M = map(int, input().split())
matrix = [[0 for _ in range(C)] for __ in range(R)]
bowl = deepcopy(matrix)
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    bowl[r - 1][c - 1] = (z, s, d - 1)


def move_fisherman(n):
    catch = 0
    for i in range(R):
        if bowl[i][n] and not catch:
            catch = bowl[i][n][0]
            bowl[i][n] = 0
    return catch


def move_sharks(bowl):
    new_bowl = deepcopy(matrix)
    for r in range(R):
        for c in range(C):
            if bowl[r][c]:
                z, s, d = bowl[r][c]
                nr, nc, nd = move_one_shark(r, c, s, d)
                if new_bowl[nr][nc] == 0:
                    new_bowl[nr][nc] = (z, s, nd)
                else:
                    nbz, nbs, nbd = new_bowl[nr][nc]
                    if nbz > z:
                        continue
                    else:
                        new_bowl[nr][nc] = (z, s, nd)
    return new_bowl


def move_one_shark(r, c, s, d):
    if d == 0:
        move_val = s % (2 * (R - 1))
        if 0 <= r - move_val < R:
            r = r - move_val
        elif 0 <= r - move_val + R - 1 < R:
            r = move_val - r
            d = 1
        else:
            r = 2 * (R - 1) + r - move_val
    elif d == 1:
        move_val = s % (2 * (R - 1))
        if 0 <= r + move_val < R:
            r = r + move_val
        elif 0 <= r + move_val - R + 1 < R:
            r = 2 * (R - 1) - move_val - r
            d = 0
        else:
            r = r + move_val - 2 * (R - 1)
    elif d == 2:
        move_val = s % (2 * (C - 1))
        if 0 <= c + move_val < C:
            c = c + move_val
        elif 0 <= c + move_val - C + 1 < C:
            c = 2 * (C - 1) - move_val - c
            d = 3
        else:
            c = c + move_val - 2 * (C - 1)
    elif d == 3:
        move_val = s % (2 * (C - 1))
        if 0 <= c - move_val < C:
            c = c - move_val
        elif 0 <= c - move_val + C - 1 < C:
            c = move_val - c
            d = 2
        else:
            c = 2 * (C - 1) + c - move_val
    return r, c, d


catch_val = 0
for i in range(C):
    catch_val += move_fisherman(i)
    bowl = move_sharks(bowl)
print(catch_val)

