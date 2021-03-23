import sys


def prime(n):
    prime = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if prime[i] is True:
            for j in range(2 * i, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] is True]


p = prime(10001)
n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    diff = 10001
    a = 0
    b = 0
    for i in range(len(p)):
        if p[i] >= m / 2:
            if m - p[i] in p:
                a = p[i]
                b = m - p[i]
                break
    print(b, a)

