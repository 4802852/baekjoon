import sys

n, k = map(int, sys.stdin.readline().split())
wl = [0]
vl = [0]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    wl.append(w)
    vl.append(v)
dp = [[0 for _ in range(k + 1)] for __ in range(n + 1)]
for i in range(n + 1):
    for j in range(k + 1):
        if j - wl[i] >= 0:
            dp[i][j] = max(dp[i - 1][j - wl[i]] + vl[i], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])
