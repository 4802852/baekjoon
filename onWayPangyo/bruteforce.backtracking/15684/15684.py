import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, M, H = map(int, input().split(" "))
ladder = [[0] * (H + 1) for _ in range(N + 1)]


def check():
    for i in range(1, N + 1):
        if getResult(i) != i:
            return False
    return True


def getResult(idx):
    i = idx
    for j in range(1, H + 1):
        if ladder[i][j] == 1:
            i += 1
        elif ladder[i - 1][j] == 1:
            i -= 1
    return i


def dfs(depth, idx):
    global ans
    if depth >= ans:
        return
    if check():
        ans = depth
        return
    for c in range(idx, len(ladder_list)):
        i, j = ladder_list[c]
        if ladder[i - 1][j] == 1 or ladder[i + 1][j] == 1:
            continue
        ladder[i][j] = 1
        dfs(depth + 1, c + 1)
        ladder[i][j] = 0


def solve():
    global ans, ladder_list
    for _ in range(M):
        b, a = map(int, input().split(" "))
        ladder[a][b] = 1
    ladder_list = []
    for i in range(1, N):
        for j in range(1, H + 1):
            if ladder[i][j] == 1 or ladder[i + 1][j] == 1 or ladder[i - 1][j] == 1:
                continue
            ladder_list.append([i, j])
    ans = 4
    dfs(0, 0)
    print(ans if ans < 4 else -1)


solve()
