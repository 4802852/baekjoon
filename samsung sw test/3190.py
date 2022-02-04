import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사
from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1
L = int(input())
turn = []
for _ in range(L):
    X, C = input().split()
    turn.append((int(X), C))
rc = [0, 1, 0, -1]
cc = [1, 0, -1, 0]
snake = deque([(0, 0)])
board[0][0] = 2


def move(di):
    nr, nc = snake[-1][0] + rc[di], snake[-1][1] + cc[di]
    if not (0 <= nr < N and 0 <= nc < N):
        return 0
    elif board[nr][nc] == 2:
        return 0
    elif board[nr][nc] == 1:
        snake.append((nr, nc))
        board[nr][nc] = 2
    else:
        snake.append((nr, nc))
        board[nr][nc] = 2
        dr, dc = snake.popleft()
        board[dr][dc] = 0
    return 1


def solve():
    time = 0
    res = 1
    di = 0
    turn_time = 0
    while res:
        res = move(di)
        time += 1
        if turn_time == len(turn):
            pass
        elif time == turn[turn_time][0]:
            if turn[turn_time][1] == "D":
                di += 1
            else:
                di -= 1
            di %= 4
            turn_time += 1
    print(time)


solve()
