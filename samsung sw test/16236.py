import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from collections import deque

rc = [0, 1, 0, -1]
cc = [1, 0, -1, 0]
N = int(input())
tank = []
fish = [[] for _ in range(7)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 0:
            continue
        elif tmp[j] == 9:
            shark_r, shark_c = i, j
        else:
            fish[tmp[j]].append((i, j))
    tank.append(tmp)
shark_level = 2
tank[shark_r][shark_c] = 0


def find_route(shark_r, shark_c, level, target_list):
    # 현재 상어의 위치와 레벨, 그리고 먹을 수 있는 물고기 리스트가 주어졌을 때, 최단 거리 물고기까지의 거리를 구한다.
    min_val = float("inf")
    ans_list = []
    queue = deque([])
    visited = [[0] * N for _ in range(N)]
    queue.append((shark_r, shark_c, 0))
    visited[shark_r][shark_c] = 1
    while queue:
        r, c, distance = queue.popleft()
        if distance > min_val:
            # 상어로부터의 거리가 이미 구해진 다른 물고기의 최단거리보다 클 경우 계산을 중단한다.
            continue
        for i in range(4):
            nr, nc = r + rc[i], c + cc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if (nr, nc) in target_list:
                    # 다음 위치가 먹을 수 있는 물고기 목록에 있다면 정답 리스트에 추가하고,
                    # 목표 물고기 최단거리를 갱신하여 이보다 멀리있는 물고기에 대한 거리는 계산하지 않도록 한다.
                    ans_list.append((distance + 1, nr, nc))
                    min_val = distance + 1
                if tank[nr][nc] <= level and not visited[nr][nc]:
                    queue.append((nr, nc, distance + 1))
                    visited[nr][nc] = 1
    if ans_list:
        return sorted(ans_list)[0]
    else:
        # 인덱스에러 수정: 먹을 수 있는 물고기는 있지만 해당 위치에 도달할 수 없는 경우 인덱스에러가 발생하게 된다.
        return (0, 0, 0)


def find_next(r, c, level):
    tmp = []
    # 먹을 수 있는 물고기 목록을 저장한다.
    for i in range(1, level):
        tmp += fish[i]
    if tmp:
        # 먹을 수 있는 물고기가 있을 경우, 먹을 수 있는 물고기중에 기준에 충족하는 물고기를 구하는 find_route 함수에 입력해준다.
        distance, tr, tc = find_route(r, c, level, tmp)
        return (distance, tr, tc)
    else:
        # 먹을 수 있는 물고기가 없을 경우 0을 리턴하여 구분해준다.
        return (0, 0, 0)


total_distance = 0
flag = 1
while flag:
    for i in range(shark_level):
        d, tr, tc = find_next(shark_r, shark_c, shark_level)
        if d == 0:
            # d의 리턴값이 0일 경우는 두가지다. 먹을 수 있는 물고기가 없거나, 있지만 도달할 수 없을 경우.
            flag = 0
            break
        # 목표 물고기가 정해졌을 경우 해당 물고기를 먹고 상어는 해당 위치로 이동하며 이동거리를 합산해준다.
        fish[tank[tr][tc]].remove((tr, tc))
        tank[tr][tc] = 0
        total_distance += d
        shark_r, shark_c = tr, tc
    shark_level += 1
    if shark_level > 7:
        shark_level = 7
print(total_distance)
