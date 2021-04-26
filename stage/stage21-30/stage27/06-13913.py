import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[-1, -1] for _ in range(100001)]
dp[n][0] = 0
q = [n]
while dp[k][0] == -1:
    now = q.pop(0)
    if 0 <= now - 1 <= 100000 and dp[now - 1][0] == -1:
        q.append(now - 1)
        dp[now - 1] = [dp[now][0] + 1, now]
    if 0 <= now + 1 <= 100000 and dp[now + 1][0] == -1:
        q.append(now + 1)
        dp[now + 1] = [dp[now][0] + 1, now]
    if 0 <= now * 2 <= 100000 and dp[now * 2][0] == -1:
        q.append(now * 2)
        dp[now * 2] = [dp[now][0] + 1, now]
now = k
order = [k]
while now != n:
    order.append(dp[now][1])
    now = dp[now][1]
print(dp[k][0])
print(*order[::-1])