import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))
minimum = 64
check1 = 0
check2 = 0
ans = []
for i in range(n - 7):
    ans.append([])
    for j in range(m - 7):
        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0:
                    if board[i + k][j + l] == 'B':
                        check1 += 1
                    else:
                        check2 += 1
                else:
                    if board[i + k][j + l] == 'W':
                        check1 += 1
                    else:
                        check2 += 1
        ans[i].append(min(check1, check2))
        check1 = 0
        check2 = 0
for i in range(len(ans)):
    if min(ans[i]) < minimum:
        minimum = min(ans[i])
print(minimum)

"""
8 9
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBW
출력 : 32
답 : 31
"""