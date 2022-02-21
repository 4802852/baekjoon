import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from copy import deepcopy

N, M = map(int, input().split())
matrix = []
# 최초의 빈 공간의 개수(빈공간 - 감시 구역 = 사각지대), cctv의 위치를 저장
zero_count = 0
cctv = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 0:
            zero_count += 1
        elif tmp[j] == 6:
            pass
        else:
            cctv.append((i, j, tmp[j]))
    matrix.append(tmp)
min_val = [float("inf")]
rc = [-1, 0, 1, 0]
cc = [0, 1, 0, -1]
# cctv 1번~5번까지 감시 구역을 저장한 리스트 (0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽)
cctv_directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],
]


def direction(tmp_matrix, r, c, di):
    """
    주어진 구역에서 cctv가 보고 있는 방향을 따라 탐색하며 벽을 만나면 멈추고, 빈 공간일 경우 감시 구역으로 지정하며,
    탐색하는 동안 감시 구역 수를 카운트하여 리턴하는 함수
    """
    cnt = 0
    nr, nc = r + rc[di], c + cc[di]
    while 0 <= nr < N and 0 <= nc < M:
        if tmp_matrix[nr][nc] == 6:
            break
        elif tmp_matrix[nr][nc] == 0:
            tmp_matrix[nr][nc] = -1
            cnt += 1
        nr, nc = nr + rc[di], nc + cc[di]
    return cnt


def dfs(matrix, depth, cnt):
    if len(cctv) <= depth:
        # 모든 cctv의 감시 구역을 조정한 후 사각 지대의 수를 최신화
        min_val[0] = min(min_val[0], zero_count - cnt)
        return
    # depth 번째 cctv 선택
    r, c, n = cctv[depth]
    for array in cctv_directions[n]:
        # 지난 cctv까지 감시 구역이 표시된 matrix를 deepcopy
        tmp_matrix = deepcopy(matrix)
        # 현재 cctv에서 감시 구역의 수를 카운트
        tmp_count = 0
        for di in array:
            tmp_count += direction(tmp_matrix, r, c, di)
        # 감시 구역을 표시하고 다음 cctv로 dfs 진행
        dfs(tmp_matrix, depth + 1, cnt + tmp_count)


dfs(matrix, 0, 0)
print(min_val[0])
