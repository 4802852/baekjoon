import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
matrix = []
start = []
zero_list = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 2:
            start.append((i, j))
        if tmp[j] == 0:
            zero_list.append((i, j))
    matrix.append(tmp)
rc = [1, 0, -1, 0]
cc = [0, 1, 0, -1]


def solve(matrix):
    # 빈 공간 중 3개를 선택하여 벽으로 막고, 바이러스를 카운트 하는 bfs 계산을 진행하도록 하는 함수
    min_virus = float("inf")  # 최소 바이러스 감염 수를 저장
    for i in range(len(zero_list) - 2):
        matrix[zero_list[i][0]][zero_list[i][1]] = 1
        for j in range(i + 1, len(zero_list) - 1):
            matrix[zero_list[j][0]][zero_list[j][1]] = 1
            for k in range(j + 1, len(zero_list)):
                matrix[zero_list[k][0]][zero_list[k][1]] = 1
                board = deepcopy(matrix)
                res = bfs(board, min_virus)
                min_virus = min(res, min_virus)
                matrix[zero_list[k][0]][zero_list[k][1]] = 0
            matrix[zero_list[j][0]][zero_list[j][1]] = 0
        matrix[zero_list[i][0]][zero_list[i][1]] = 0
    return min_virus


def bfs(board, old_min):
    # bfs 알고리즘을 이용하여 바이러스가 침범한 공간의 수를 카운트
    queue = deque([])
    cnt_virus = 0
    for virus in start:
        queue.append(virus)
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + rc[i], c + cc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
                # 바이러스에서 이동한 공간이 연구소를 벗어나지 않으며 빈 공간이면 바이러스에 감염되었다고 표시
                board[nr][nc] = 2
                queue.append((nr, nc))
                cnt_virus += 1
        if cnt_virus >= old_min:
            # 바이러스를 카운트 하는 중에 기존 최소 바이러스 개수를 초과할 경우 계산을 중단
            return float("inf")
    return cnt_virus


ans = solve(matrix)
# 처음의 빈 공간 수 - 벽으로 막은 빈공간 수(3) - 바이러스 감염 수 = 안전 지대 개수
print(len(zero_list) - 3 - ans)
