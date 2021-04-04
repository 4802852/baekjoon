import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    wear = []
    for i in range(m):
        a, b = map(str, sys.stdin.readline().split())
        wear.append([b, a])
    wear.sort()
    wear.append([' ', ' '])
    check = [-1]
    for j in range(m):
        if wear[j][0] != wear[j + 1][0]:
            check.append(j)
    ans = 1
    for k in range(1, len(check)):
        ans *= check[k] - check[k - 1] + 1
    print(ans - 1)