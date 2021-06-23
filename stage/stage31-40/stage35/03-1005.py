import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    cost = [0] + list(map(int, sys.stdin.readline().split()))
    tree = [[] for __ in range(n + 1)]
    in_degree = [0] * (n + 1)
    dp = [0] * (n + 1)
    for __ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        in_degree[b] += 1
        tree[a].append(b)
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    while q:
        now = q.popleft()
        for i in tree[now]:
            in_degree[i] -= 1
            dp[i] = max(dp[now] + cost[i], dp[i])
            if in_degree[i] == 0:
                q.append(i)
    ans = int(sys.stdin.readline())
    print(dp[ans])