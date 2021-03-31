import sys

sys.setrecursionlimit(10**6)


fact = [1, 1] + [0 for _ in range(1000)]


def factorial(n):
    if fact[n] != 0:
        return fact[n]
    if fact[n - 1] != 0:
        fact[n] = n * fact[n - 1]
        return fact[n]
    return n * factorial(n - 1)


a, b = map(int, input().split())
c = factorial(a)
d = factorial(b)
e = factorial(a - b)
print(int((c // (d * e)) % 10007))
