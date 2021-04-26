import sys

m = [0] + list(sys.stdin.readline().rstrip())
n = [0] + list(sys.stdin.readline().rstrip())
dp = [['' for _ in range(len(n))] for __ in range(len(m))]
for i in range(1, len(m)):
    for j in range(1, len(n)):
        if m[i] == n[j]:
            dp[i][j] = dp[i - 1][j - 1] + m[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(len(dp[len(m) - 1][len(n) - 1]))
print(dp[len(m) - 1][len(n) - 1])

