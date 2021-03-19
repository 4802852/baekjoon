import sys


def prime(n):
    prime = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if prime[i] is True:
            for j in range(2 * i, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] is True]


while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    p = prime(2 * n + 1)
    count = 0
    for i in range(len(p)):
        if n < p[i]:
            count += 1
    print(count)