import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, M = map(int, input().split())
house = []
chicken = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            house.append((i, j))
        elif tmp[j] == 2:
            chicken.append((i, j))
min_val = [float("inf")]
chicken_selected = []


def check(house_list, chicken_list):
    # 현재 주어진 집 리스트와 치킨집 리스트를 비교하여 도시의 치킨거리를 리턴해주는 함수
    chicken_distance = 0
    for h_i, h_j in house_list:
        tmp = float("inf")
        for c_i, c_j in chicken_list:
            tmp = min(tmp, abs(h_i - c_i) + abs(h_j - c_j))
        chicken_distance += tmp
    return chicken_distance


def dfs(depth, index):
    if M == depth:
        # 치킨집을 M개 모두 선택했을 경우 도시의 치킨거리를 계산하여 최소값 갱신
        min_val[0] = min(min_val[0], check(house, chicken_selected))
        return
    for i in range(index + 1, len(chicken)):
        # 치킨집을 순차적으로 선택하여 선택된 치킨집으로 선정하고 dfs 를 이용하여 개수 증가
        chicken_selected.append(chicken[i])
        dfs(depth + 1, i)
        chicken_selected.remove(chicken[i])


dfs(0, -1)
print(min_val[0])
