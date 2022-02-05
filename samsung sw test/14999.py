import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, M, r, c, K = map(int, input().split())
B = []
for i in range(N):
    B.append(list(map(int, input().split())))
rc = [0, 0, 0, -1, 1]
cc = [0, 1, -1, 0, 0]
dice = [[0] * 3 for _ in range(4)]


def move_dice(di):
    if di == 1:
        tmp = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = tmp
    elif di == 2:
        tmp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif di == 3:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    elif di == 4:
        tmp = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = tmp


def move(r, c, di):
    nr, nc = r + rc[di], c + cc[di]
    if not (0 <= nr < N and 0 <= nc < M):
        return r, c
    else:
        move_dice(di)
        if B[nr][nc] == 0:
            B[nr][nc] = dice[3][1]
        else:
            dice[3][1] = B[nr][nc]
            B[nr][nc] = 0
        print(dice[1][1])
        return nr, nc


K_list = list(map(int, input().split()))
for i in range(K):
    r, c = move(r, c, K_list[i])
