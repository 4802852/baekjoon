import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
S = [list(map(int, input().split(" "))) for _ in range(N)]
visited = [0] * N
result = float("inf")


def getTeamScore(arr):
    teamScore = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            teamScore += S[arr[i]][arr[j]] + S[arr[j]][arr[i]]
    return teamScore


def getTeam(depth, i, aTeam, bTeam):
    global result
    if depth == N:
        result = min(result, abs(getTeamScore(aTeam) - getTeamScore(bTeam)))
    if len(aTeam) < N // 2:
        getTeam(depth + 1, i + 1, aTeam + [i], bTeam)
    if len(bTeam) < N // 2:
        getTeam(depth + 1, i + 1, aTeam, bTeam + [i])


getTeam(1, 1, [0], [])
print(result)
