import sys

n = int(sys.stdin.readline())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for i in range(n):
    m, n = map(int, sys.stdin.readline().split())
    print(int(m * n / gcd(m, n)))