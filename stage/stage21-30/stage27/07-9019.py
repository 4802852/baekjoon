import sys


def dslr(x):
    d1 = x // 1000
    d2 = x % 1000 // 100
    d3 = x % 100 // 10
    d4 = x % 10
    d = 2 * x % 10000
    s = x - 1 if x else 9999
    l = d2 * 1000 + d3 * 100 + d4 * 10 + d1
    r = d4 * 1000 + d1 * 100 + d2 * 10 + d3
    return [d, s, l, r]


def bfs():
    q = [a]
    while dp[b] == '':
        now = q.pop(0)
        nowLetter = dp[now]
        next = dslr(now)
        nextLetter = ['D', 'S', 'L', 'R']
        for i, n in enumerate(next):
            if dp[n] == '':
                dp[n] = nowLetter + nextLetter[i]
                q.append(n)
    return dp[b]


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    dp = [''] * 10000
    print(bfs())