import sys

fact = [1, 1] + [0 for _ in range(30)]


def factorial(n):
    if fact[n] != 0:
        return fact[n]
    if fact[n - 1] != 0:
        fact[n] = n * fact[n - 1]
        return fact[n]
    return n * factorial(n - 1)


def combination(a, b):
    c = factorial(a)
    d = factorial(b)
    e = factorial(a - b)
    return int(c // (d * e))


n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(combination(b, a))