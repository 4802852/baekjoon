import sys

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
dp = [[[0, 0, 0] for _ in range(n)] for __ in range(n)]
knuth = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    dp[i][i] = matrix[i] + [0]
for x in range(1, n):
    for i in range(n - x):
        j = i + x
        dp[i][j][2] = 2 ** 31
        dp[i][j] = [matrix[i][0], matrix[j][1], dp[i][j][2]]
        for k in range(i, j):
            dp[i][j][2] = min(dp[i][j][2], dp[i][k][2] + dp[k + 1][j][2] + dp[i][k][0] * dp[i][k][1] * dp[k + 1][j][1])
print(dp[0][n - 1][2])
