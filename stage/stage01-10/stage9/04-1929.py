import sys


def prime(n):
    prime = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if prime[i] is True:
            for j in range(2 * i, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] is True]


m, n = map(int, sys.stdin.readline().split())
p = prime(n + 1)
for i in range(len(p)):
    if m <= p[i]:
        print(p[i])