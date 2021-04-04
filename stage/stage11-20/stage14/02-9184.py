import sys


# wt = [[[0] * 21 for _ in range(21)] for __ in range(21)]
#
#
# def w(a, b, c):
#     global wt
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     if wt[a][b][c]:
#         return wt[a][b][c]
#     if a < b < c:
#         wt[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
#         return wt[a][b][c]
#     wt[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
#     return wt[a][b][c]
#
#
# while 1:
#     n, m, p = map(int, sys.stdin.readline().split())
#     if n == -1 and m == -1 and p == -1:
#         break
#     print('w({}, {}, {}) = {}'.format(n, m, p, w(n, m, p)))


wt = []
for i in range(0, 21):
    wt.append([])
    for j in range(0, 21):
        wt[i].append([])
        for k in range(0, 21):
            if i == 0 or j == 0 or k == 0:
                wt[i][j].append(1)
            else:
                if i < j < k:
                    wt[i][j].append(wt[i][j][k - 1] + wt[i][j - 1][k - 1] - wt[i][j - 1][k])
                else:
                    wt[i][j].append(wt[i - 1][j][k] + wt[i - 1][j - 1][k] + wt[i - 1][j][k - 1] - wt[i - 1][j - 1][k - 1])


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return wt[20][20][20]
    return wt[a][b][c]


while 1:
    n, m, p = map(int, sys.stdin.readline().split())
    if n == -1 and m == -1 and p == -1:
        break
    print('w({}, {}, {}) = {}'.format(n, m, p, w(n, m, p)))
