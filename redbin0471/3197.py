import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
from collections import deque


R, C = map(int, sys.stdin.readline().split())
swan = []
matrix = []
sq, sq_t, wq, wq_t = deque(), deque(), deque(), deque()
for i in range(R):
    matrix.append(list(sys.stdin.readline().strip()))
    for j in range(C):
        if matrix[i][j] == "L":
            swan.append((i, j))
            wq.append((i, j))
            matrix[i][j] = 0
        elif matrix[i][j] == ".":
            # 물을 입력받을 때 물 큐에 미리 추가하여 시간을 아낄 수 있다.
            matrix[i][j] = 0
            wq.append((i, j))
        else:
            matrix[i][j] = 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
swan_visited = [[0] * C for _ in range(R)]
sr, sc = swan[0]
er, ec = swan[1]


def SwanBFS():
    while sq:
        now_r, now_c = sq.popleft()
        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            if nr == er and nc == ec:
                return 0
            if nr < 0 or R <= nr or nc < 0 or C <= nc or swan_visited[nr][nc] == 1:
                continue
            swan_visited[nr][nc] = 1
            # 다음 위치가 물이라면 물 큐에 넣어 탐색을 계속하고, 다음 위치가 얼음이라면 백조가 가지 못하는 얼음의 가장자리이므로 임시 큐에 추가해준다.
            if matrix[nr][nc] == 0:
                sq.append((nr, nc))
            else:
                sq_t.append((nr, nc))
    return 1


def Melt():
    while wq:
        r, c = wq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or R <= nr or nc < 0 or C <= nc or matrix[nr][nc] == 0:
                continue
            # 물에서 가까운 얼음의 가장자리를 물 임시 큐에 추가해준다.
            wq_t.append((nr, nc))
            matrix[nr][nc] = 0


swan_visited[sr][sc] = 1
sq.append((sr, sc))
ans = 0
while SwanBFS():
    ans += 1
    Melt()
    sq, wq = sq_t, wq_t
    sq_t, wq_t = deque(), deque()
print(ans)
