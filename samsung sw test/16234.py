import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from collections import deque

rc = [0, 1, 0, -1]
cc = [1, 0, -1, 0]
N, L, R = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


def link(r, c):
    queue = deque([])
    queue.append((r, c))
    visited[r][c] = 1
    linked = [(r, c)]
    sum = matrix[r][c]
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + rc[i], c + cc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(matrix[nr][nc] - matrix[r][c]) <= R:
                    linked.append((nr, nc))
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    sum += matrix[nr][nc]
    linked_val = sum // len(linked)
    for i in range(len(linked)):
        matrix[linked[i][0]][linked[i][1]] = linked_val


cnt = 0
while 1:
    visited = [[0] * N for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                flag = False
                continue
            link(i, j)
    if flag:
        break
    else:
        cnt += 1
print(cnt)
