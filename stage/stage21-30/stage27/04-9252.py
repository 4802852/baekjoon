import sys

m = [0] + list(sys.stdin.readline().rstrip())
n = [0] + list(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(len(n))] for __ in range(len(m))]
for i in range(1, len(m)):
    for j in range(1, len(n)):
        if m[i] == n[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

row = len(m) - 1
col = len(n) - 1
ans = ""
while dp[row][col]:
    if dp[row][col] == dp[row - 1][col]:
        row -= 1
    elif dp[row][col] == dp[row][col - 1]:
        col -= 1
    else:
        ans = m[row] + ans
        row -= 1
        col -= 1

print(dp[len(m) - 1][len(n) - 1])
print(ans)
