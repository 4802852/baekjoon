import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from copy import deepcopy

dice = list(map(int, input().split()))
# board_dict  k: location, v: next_location_list([dice_1, dice_2, dice_3, dice_4, dice_5])
board_dict = {}
# 말이 이동하여 보드판 바깥으로 나갈 경우 -1로 표기
for i in range(21):
    tmp = []
    for j in range(1, 6):
        tmp.append(i + j if i + j < 21 else -1)
    board_dict[i] = tmp
board_dict[5] = [21, 22, 23, 29, 30]
board_dict[21] = [22, 23, 29, 30, 31]
board_dict[22] = [23, 29, 30, 31, 20]
board_dict[23] = [29, 30, 31, 20, -1]
board_dict[10] = [24, 25, 29, 30, 31]
board_dict[24] = [25, 29, 30, 31, 20]
board_dict[25] = [29, 30, 31, 20, -1]
board_dict[15] = [26, 27, 28, 29, 30]
board_dict[26] = [27, 28, 29, 30, 31]
board_dict[27] = [28, 29, 30, 31, 20]
board_dict[28] = [29, 30, 31, 20, -1]
board_dict[29] = [30, 31, 20, -1, -1]
board_dict[30] = [31, 20, -1, -1, -1]
board_dict[31] = [20, -1, -1, -1, -1]
# score_dict  k: location, v: score
score_dict = {
    21: 13,
    22: 16,
    23: 19,
    24: 22,
    25: 24,
    26: 28,
    27: 27,
    28: 26,
    29: 25,
    30: 30,
    31: 35,
    -1: 0,
}
for i in range(1, 21):
    score_dict[i] = i * 2
locations = [0] * 4
ans = []


def dfs(prev_number, location_list, depth):
    if len(dice) <= depth:
        # 말의 모든 이동이 끝날 경우 총 합을 ans에 추가
        ans.append(prev_number)
        return
    for i in range(4):
        if location_list[i] == -1:
            # 말이 도착점에 있을 경우 continue
            continue
        ne_lo = board_dict[location_list[i]][dice[depth] - 1]
        next_location = deepcopy(location_list)
        if ne_lo != -1 and ne_lo in location_list:
            # 말이 이동하려는 위치에 다른 말이 있을 경우 continue
            continue
        next_location[i] = ne_lo
        dfs(prev_number + score_dict[next_location[i]], next_location, depth + 1)


dfs(0, locations, 0)
print(max(ans))
