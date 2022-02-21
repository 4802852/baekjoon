import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사


N, M, H = map(int, input().split())
ladder = [[0] * H for _ in range(N - 1)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ladder[b][a] = 1
    if b < N - 2:
        ladder[b + 1][a] = -1
    if 0 < b:
        ladder[b - 1][a] = -1
possible_ladder = []
for i in range(N - 1):
    for j in range(H):
        if ladder[i][j] == 0:
            possible_ladder.append((i, j))
min_val = [4]


def ladder_down(s):
    p = 0
    while p < H:
        if s < N - 1 and ladder[s][p] == 1:
            s += 1
        elif 0 < s and ladder[s - 1][p] == 1:
            s -= 1
        p += 1
    return s


def check():
    flag = True
    s = 0
    while flag and s < N:
        if s != ladder_down(s):
            flag = False
        s += 1
    return flag


def solve(depth, position_list, index):
    if min_val[0] <= depth or 3 < depth:
        return
    if check():
        min_val[0] = min(min_val[0], depth)
    for i in range(index + 1, len(position_list)):
        r, c = position_list[i]
        if r < N - 2 and ladder[r + 1][c] == 1:
            continue
        if 0 < r and ladder[r - 1][c] == 1:
            continue
        ladder[r][c] = 1
        solve(depth + 1, position_list, i)
        ladder[r][c] = 0


solve(0, possible_ladder, -1)
if min_val[0] == 4:
    print(-1)
else:
    print(min_val[0])
