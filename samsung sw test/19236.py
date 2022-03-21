import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from copy import deepcopy

rc = [-1, -1, 0, 1, 1, 1, 0, -1]
cc = [0, -1, -1, -1, 0, 1, 1, 1]
bowl = []
fish = {}
for i in range(4):
    tmp = list(map(int, input().split()))
    tmp2 = []
    for j in range(4):
        tmp2.append(tmp[2 * j])
        fish[tmp[2 * j]] = [i, j, tmp[2 * j + 1] - 1]
    bowl.append(tmp2)
eat_fish_number = bowl[0][0]
sr, sc, sd = fish.pop(bowl[0][0])
bowl[0][0] = 0
fish[-1] = [0, 0, sd]
ans = []


def move(bowl_arr, fish_dict):
    for n in range(1, 17):
        if n not in fish_dict.keys():
            continue
        r, c, d = fish_dict[n]
        nr, nc = r + rc[d], c + cc[d]
        while (
            nr < 0
            or 4 <= nr
            or nc < 0
            or 4 <= nc
            or (nr == fish_dict[-1][0] and nc == fish_dict[-1][1])
        ):
            d = (d + 1) % 8
            nr, nc = r + rc[d], c + cc[d]
        fish_to_change = bowl_arr[nr][nc]
        if fish_to_change == 0:
            pass
        else:
            cnr, cnc, cd = fish_dict[fish_to_change]
            fish_dict[fish_to_change] = [r, c, cd]
        fish_dict[n] = [nr, nc, d]
        bowl_arr[r][c] = fish_to_change
        bowl_arr[nr][nc] = n


def shark_move_dfs(bowl_arr, fish_dict, prev_number):
    ans.append(prev_number)
    move(bowl_arr, fish_dict)
    sr, sc, sd = fish_dict[-1]
    for i in range(1, 4):
        n_bowl_arr = deepcopy(bowl_arr)
        n_fish_dict = deepcopy(fish_dict)
        nsr, nsc = sr + rc[sd] * i, sc + cc[sd] * i
        if nsr < 0 or 4 <= nsr or nsc < 0 or 4 <= nsc:
            continue
        if n_bowl_arr[nsr][nsc] == 0:
            continue
        to_eat = n_bowl_arr[nsr][nsc]
        nsr, nsc, nsd = n_fish_dict.pop(to_eat)
        n_bowl_arr[nsr][nsc] = 0
        n_fish_dict[-1] = [nsr, nsc, nsd]
        shark_move_dfs(n_bowl_arr, n_fish_dict, prev_number + to_eat)


shark_move_dfs(bowl, fish, eat_fish_number)
print(max(ans))
