import sys


def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1
    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
        return 1
    return 0


n = int(sys.stdin.readline())
lines = [[]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
parent = [-1 for _ in range(n + 1)]


def find(x):
    if parent[x] < 0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


for i in range(1, n):
    for j in range(i + 1, n + 1):
        x1, y1, x2, y2 = lines[i]
        x3, y3, x4, y4 = lines[j]
        if check(x1, y1, x2, y2, x3, y3, x4, y4):
            union(i, j)

cnt = 0
maxVal = 0
for i in parent[1:]:
    if i < 0:
        cnt += 1
        maxVal = max(maxVal, abs(i))
print(cnt)
print(maxVal)