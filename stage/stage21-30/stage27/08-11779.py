import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a][b] = min(bus[a][b], c)
s, e = map(int, sys.stdin.readline().split())
dp = [[float("inf"), -1] for _ in range(n + 1)]
dp[s] = [0, 0]
q = [s]
while q:
    now = q.pop(0)
    for dest in range(1, n + 1):
        if dp[now][0] + bus[now][dest] < dp[dest][0]:
            dp[dest][0] = dp[now][0] + bus[now][dest]
            dp[dest][1] = now
            q.append(dest)
print(dp[e][0])
res = [e]
tmp = e
while tmp != s:
    res.append(dp[tmp][1])
    tmp = dp[tmp][1]
print(len(res))
print(*res[::-1])
