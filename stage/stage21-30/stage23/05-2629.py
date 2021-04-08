import sys

n = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
possible = []
ans = [[0 for _ in range(15001)] for __ in range(n + 1)]


def scale(weight, n, now, left, right):
    new = abs(left - right)
    if new not in possible:
        possible.append(new)
    if now == n:
        return 0
    if ans[now][new] == 0:
        scale(weight, n, now + 1, left + weight[now], right)
        scale(weight, n, now + 1, left, right + weight[now])
        scale(weight, n, now + 1, left, right)
        ans[now][new] = 1


scale(weight, n, 0, 0, 0)
for i in check:
    if i in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')
