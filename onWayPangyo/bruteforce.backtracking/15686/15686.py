import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from itertools import combinations as cb

N, M = map(int, input().split(" "))
house = []
chicken = []
for i in range(N):
    line = list(map(int, input().split(" ")))
    for j in range(N):
        if line[j] == 1:
            house.append([i, j])
        elif line[j] == 2:
            chicken.append([i, j])


def getDist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


chickenDistance = [[] for _ in range(len(house))]
for i in range(len(house)):
    hr, hc = house[i]
    for j in range(len(chicken)):
        cr, cc = chicken[j]
        chickenDistance[i].append((getDist(hr, hc, cr, cc), j))
    chickenDistance[i].sort()


def getChickenDistance(arr):
    global ans
    tmp = 0
    for i in chickenDistance:
        for j in i:
            if j[1] in arr:
                tmp += j[0]
                break
        if tmp >= ans:
            return
    ans = min(ans, tmp)


num_arr = [i for i in range(len(chicken))]
ans = float("inf")
for l in cb(num_arr, M):
    getChickenDistance(l)
print(ans)
