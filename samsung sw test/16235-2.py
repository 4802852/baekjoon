import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
from copy import deepcopy

rc = [0, 1, 1, 1, 0, -1, -1, -1]
cc = [1, 1, 0, -1, -1, -1, 0, 1]
N, M, K = map(int, sys.stdin.readline().split())
soil = [[5] * N for _ in range(N)]
# 나무를 저장하는 tree의 각 위치에 dictionary를 이용하고, 해당 dictionary에 {나이: 해당 나이의 나무 수} 의 형태로 저장해준다.
tree = [[{} for _ in range(N)] for __ in range(N)]
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x - 1][y - 1][z] = 1

while K:
    # 연간 주어야 하는 비료를 A를 복제함으로써 초기화해주고, 비료가 되는 나무들을 추가해준다.
    fertilizer = deepcopy(A)
    for r in range(N):
        for c in range(N):
            if tree[r][c]:
                tmp = {}
                fertile = 0
                for age in sorted(tree[r][c].keys()):
                    # 나이 적은 나무 순서대로 탐색하여 양분이 부족해질때까지 나무에 양분을 주고, 나머지는 비료로 추가한다.
                    if age * tree[r][c][age] <= soil[r][c]:
                        soil[r][c] -= age * tree[r][c][age]
                        tmp[age + 1] = tree[r][c][age]
                    else:
                        survive = soil[r][c] // age
                        if not survive:
                            fertile += (age // 2) * tree[r][c][age]
                            continue
                        soil[r][c] -= age * survive
                        tmp[age + 1] = survive
                        fertile += (age // 2) * (tree[r][c][age] - survive)
                tree[r][c] = tmp
                fertilizer[r][c] += fertile
    for r in range(N):
        for c in range(N):
            if tree[r][c]:
                num = 0
                for age in tree[r][c].keys():
                    # 나무의 나이가 5의 배수인 나무들의 수를 모두 더해주고,
                    if age % 5 == 0:
                        num += tree[r][c][age]
                if num:
                    # 해당 위치의 8방향에 구해진 나무 수만큼 나이가 1인 나무를 더해준다.
                    for i in range(8):
                        nr, nc = r + rc[i], c + cc[i]
                        if 0 <= nr < N and 0 <= nc < N:
                            if 1 not in tree[nr][nc].keys():
                                tree[nr][nc][1] = num
                            else:
                                tree[nr][nc][1] += num
            # 비료를 더해준다.
            soil[r][c] += fertilizer[r][c]
    K -= 1
number = 0
for r in range(N):
    for c in range(N):
        number += sum(tree[r][c].values())
print(number)
