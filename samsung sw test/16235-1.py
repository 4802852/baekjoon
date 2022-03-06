import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
from copy import deepcopy
from collections import deque

rc = [0, 1, 1, 1, 0, -1, -1, -1]
cc = [1, 1, 0, -1, -1, -1, 0, 1]
N, M, K = map(int, sys.stdin.readline().split())
soil = [[5] * N for _ in range(N)]
# 나무를 저장하는 tree의 각 위치에 deque를 이용하고, 해당 위치의 나무들의 나이를 오름차순으로 저장해준다.
tree = [[deque() for _ in range(N)] for __ in range(N)]
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x - 1][y - 1].append(z)

while K:
    # 1년에 주어야 하는 비료의 기본값을 A함수를 복제함으로써 초기화하고, 나무들을 순환하며 비료가 되는 나무들을 추가해준다.
    fertile = deepcopy(A)
    seed = []
    for r in range(N):
        for c in range(N):
            len_t = len(tree[r][c])
            for k in range(len_t):
                # (r, c) 땅 위치의 나무들을 나이 작은 순서대로 순차적으로 탐색한다.
                age = tree[r][c][k]
                if soil[r][c] >= age:
                    # 땅에 남은 양분이 나무의 나이보다 크다면, 땅에서 나이만큼 양분을 먹고 나이를 늘려준다.
                    soil[r][c] -= age
                    tree[r][c][k] += 1
                    if (age + 1) % 5 == 0:
                        # 늘려준 나이가 5의 배수라면 가을에 씨앗을 뿌릴 나무를 저장해준다.
                        seed.append((r, c))
                else:
                    # 땅에 양분이 없다면 남은 나무들을 모두 거름으로 만들어 fertile matrix에 추가해주고 break
                    for _ in range(k, len_t):
                        fertile[r][c] += tree[r][c].pop() // 2
                    break
    for (r, c) in seed:
        # 씨앗 뿌릴 나무들의 8방향을 탐색하여 나이가 1인 나무를 추가해준다.
        for i in range(8):
            nr, nc = r + rc[i], c + cc[i]
            if 0 <= nr < N and 0 <= nc < N:
                tree[nr][nc].appendleft(1)
    for r in range(N):
        for c in range(N):
            # 모든 위치를 탐색하여 비료 추가해준다.
            soil[r][c] += fertile[r][c]
    K -= 1
number = 0
for r in range(N):
    for c in range(N):
        number += len(tree[r][c])
print(number)
