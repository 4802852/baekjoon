# python으로 시간초과 계속되어 pypy3으로 통과. 최적화 더 할게 남아있는지..?

import sys

n = int(sys.stdin.readline())
board = [0] * n
ans_count = 0
visited = [False] * n


def check(x):
    for i in range(x):
        if abs(board[x] - board[i]) == x - i:
            return False
    return True


def n_queen(x):
    global ans_count
    if x == n:
        ans_count += 1
        return
    for i in range(n):
        if visited[i]:
            continue

        board[x] = i
        if check(x):
            visited[i] = True
            n_queen(x + 1)
            visited[i] = False


n_queen(0)
print(ans_count)
