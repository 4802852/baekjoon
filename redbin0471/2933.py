import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
matrix = []
for _ in range(R):
    tmp = list(input().strip())
    for i in range(C):
        if tmp[i] == ".":
            tmp[i] = 0
        else:
            tmp[i] = 1
    matrix.append(tmp)
N = int(input())
h_list = list(map(int, input().split()))
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def PrintMap():
    for line in matrix:
        for j in line:
            print("." if j == 0 else "x", end="")
        print()


# (r, c) 에서 시작하는 클러스터가 공중에 떠있는지 아닌지 판펼하는 함수. 공중에 떠있다면 1, [공중에 떠있는 미네랄 좌표 리스트] 를 리턴
def is_on_air(r, c):
    # queue1은 bfs 알고리즘에 사용, queue2는 좌표 리스트
    queue1, queue2 = deque(), deque()
    queue1.append((r, c))
    queue2.append((r, c))
    visited[r][c] = 1
    while queue1:
        now_r, now_c = queue1.popleft()
        for i in range(4):
            nr, nc = now_r + dr[i], now_c + dc[i]
            if (
                nr < 0
                or R <= nr
                or nc < 0
                or C <= nc
                or matrix[nr][nc] == 0
                or visited[nr][nc] == 1
            ):
                continue
            visited[nr][nc] = 1
            queue1.append((nr, nc))
            queue2.append((nr, nc))
    # 좌표 리스트 중에 r 값이 R - 1인 값이 있다면 그 클러스터는 바닥에 닿아있으므로 0 리턴
    for r, c in queue2:
        if r == R - 1:
            return 0, []
    return 1, queue2


# 높이 h에 좌우 값을 입력받아 미네랄의 움직임을 처리하는 함수
def throw(h, LR):
    global visited
    # 부서지는 미네랄 좌표 탐색
    br = R - h
    try:
        if LR == -1:
            bc = matrix[br].index(1)
        else:
            bc = C - 1 - matrix[br][::-1].index(1)
    except:
        # 부서지는 미네랄 없다면 종료
        return
    # 부서지는 미네랄 기준 상하좌우에 있는 미네랄의 클러스터가 공중에 떠있는지 아닌지 판별 진행
    matrix[br][bc] = 0
    visited = [[0] * C for _ in range(R)]
    queue = []
    for i in range(4):
        nr, nc = br + dr[i], bc + dc[i]
        if (
            nr < 0
            or R <= nr
            or nc < 0
            or C <= nc
            or matrix[nr][nc] == 0
            or visited[nr][nc] == 1
        ):
            continue
        flag, queue = is_on_air(nr, nc)
        if flag:
            break
    # 공중에 떠있는 미네랄이 없다면 함수 종료
    if len(queue) == 0:
        return
    # 공중에 떠있는 미네랄이 몇칸 떨어질 수 있는지 fall에 저장
    for r, c in queue:
        matrix[r][c] = 0
    fall = 0
    air = 1
    while air:
        fall += 1
        for r, c in queue:
            if r + fall == R or matrix[r + fall][c] == 1:
                air = 0
                break
    fall -= 1
    for r, c in queue:
        matrix[r + fall][c] = 1


thrower = -1
for height in h_list:
    throw(height, thrower)
    thrower *= -1
PrintMap()
