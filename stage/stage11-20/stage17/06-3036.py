import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(sys.stdin.readline())
ring = list(map(int, sys.stdin.readline().split()))
prev = 1
x = 1
y = 1
for i in range(n - 1):
    x *= ring[i]
    y *= ring[i + 1]
    m = gcd(x, y)
    print('{}/{}'.format(x // m, y // m))
