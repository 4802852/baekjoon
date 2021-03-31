import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, m = map(int, sys.stdin.readline().split())
nmgcd = gcd(n, m)
print('{} {}'.format(nmgcd, int(n * m / nmgcd)))