import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from collections import deque

rc = [1, 0, -1, 0]
cc = [0, 1, 0, -1]


def move(r, c, di):
    cnt = 0
    while matrix[r + rc[di]][c + cc[di]] != '#' and matrix[r][c] == 'O':
        r += rc[di]
        c + cc[di]
        cnt += 1
    return r, c, cnt

def solve(rr, cr, rb, cb):
    queue = deque([])
    queue.append((rr, cr, rb, cb, 1))
    visited[rr][cr][rb][cb] = True
    while queue:
        rr, cr, rb, cb, depth = queue.popleft()
        if depth > 10:
            break
        for di in range(4):
            nrr, ncr, rcnt = move(rr, cr, di)
            nrb, ncb, bcnt = move(rb, cb, di)
            if matrix[nrb][ncb] != 'O':
                if matrix[nrr][ncr] == 'O':
                    return depth
                if nrr == nrb and ncr == ncb:
                    if rcnt > bcnt:
                        nrr -= rc[di]
                        ncr -= cc[di]
                    else:
                        nrb -= rc[di]
                        ncb -= cc[di]
                if not visited[nrr][ncr][nrb][ncb]:
                    visited[nrr][ncr][nrb][ncb] = True
                    queue.append((nrr, ncr, nrb, ncb, depth + 1))
    return -1

N, M = map(int, input().split())
matrix = [[""] * M for _ in range(N)]
for i in range(N):
    line_tmp = list(input())
    for j in range(M):
        if line_tmp[j] == "R":
            rr, cr = i, j
        if line_tmp[j] == "B":
            rb, cb = i, j
        if line_tmp[j] == "O":
            ro, co = i, j
        matrix[i][j] = line_tmp[j]
    visited = [[[[False] * M for _ in range(N)] for __ in range(M)] for ___ in range(N)]
    res = solve(rr, cr, rb, cb)
    print(res)
