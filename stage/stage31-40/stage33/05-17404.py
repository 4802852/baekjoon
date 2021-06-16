import sys

INF = float('inf')
n = int(sys.stdin.readline())
cost = []
for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    cost.append([r, g, b])
minVal = INF

for i in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]

    for j in range(3):
        if j == i:
            dp[0][j] = cost[0][j]
            continue
        dp[0][j] = INF

    for j in range(1, n):
        dp[j][0] = cost[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = cost[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = cost[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    for j in range(3):
        if j == i:
            continue
        minVal = min(minVal, dp[-1][j])

print(minVal)
