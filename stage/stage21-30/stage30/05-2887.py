import sys


def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    parent[y] = x


n = int(sys.stdin.readline())
parent = [i for i in range(n + 1)]
lines = []
stars = []
for i in range(1, n + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    stars.append([a, b, c, i])
for j in range(3):
    stars.sort(key=lambda x: x[j])
    for i in range(1, n):
        lines.append((abs(stars[i - 1][j] - stars[i][j]), stars[i - 1][3], stars[i][3]))
lines.sort()
cnt = 0
ans = 0
for co in lines:
    d, a, b = co
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        ans += d
        cnt += 1
    if cnt == n - 1:
        break
print(ans)
