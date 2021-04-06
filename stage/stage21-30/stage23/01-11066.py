import sys

m = int(sys.stdin.readline())
for ___ in range(m):
    n = int(sys.stdin.readline())
    pages = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for __ in range(n)] for _ in range(n)]
    for x in range(1, n):
        for i in range(n - x):
            j = i + x
            dp[i][j] = 999999999999
            tmp = sum(pages[i: j + 1])
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + tmp)
    print(dp[0][n - 1])


# Knuth's Optimization
m = int(sys.stdin.readline())
for ___ in range(m):
    n = int(sys.stdin.readline())
    pages = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for __ in range(n)] for _ in range(n)]
    knuth = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        knuth[i][i] = i
    for x in range(1, n):
        for i in range(n - x):
            j = i + x
            dp[i][j] = 999999999999
            tmp = sum(pages[i: j + 1])
            for k in range(knuth[i][j - 1], knuth[i + 1][j] + 1):
                if k < n - 1 and dp[i][j] > dp[i][k] + dp[k + 1][j] + tmp:
                    dp[i][j] = dp[i][k] + dp[k + 1][j] + tmp
                    knuth[i][j] = k
    print(dp[0][n - 1])