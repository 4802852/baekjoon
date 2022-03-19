import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def rotate(x, d, k):
    i = 1
    cnt = x - 1
    while cnt < N:
        for _ in range(k):
            if d == 0:
                board[cnt] = [board[cnt][-1]] + board[cnt][:-1]
            elif d == 1:
                board[cnt] = board[cnt][1:] + [board[cnt][0]]
        i += 1
        cnt = x * i - 1


def delete():
    delete_list = set([])
    total = 0
    cnt = 0
    for i in range(N - 1):
        for j in range(M):
            ij, ij1, ij2 = board[i][j], board[i][(j + 1) % M], board[i + 1][j]
            if ij:
                total += ij
                cnt += 1
                if ij == ij1:
                    delete_list.add((i, j))
                    delete_list.add((i, (j + 1) % M))
                if ij == ij2:
                    delete_list.add((i, j))
                    delete_list.add((i + 1, j))
    for j in range(M):
        ij, ij1 = board[N - 1][j], board[N - 1][(j + 1) % M]
        if ij:
            total += ij
            cnt += 1
            if ij == ij1:
                delete_list.add((N - 1, j))
                delete_list.add((N - 1, (j + 1) % M))
    if delete_list:
        for i, j in delete_list:
            total -= board[i][j]
            board[i][j] = 0
            cnt -= 1
    elif cnt == 0:
        return 0
    else:
        average = total / cnt
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    if board[i][j] < average:
                        board[i][j] += 1
                        total += 1
                    elif average < board[i][j]:
                        board[i][j] -= 1
                        total -= 1
    return total


for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    res = delete()
print(res)
