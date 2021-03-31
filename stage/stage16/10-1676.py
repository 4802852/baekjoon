import sys

fact = [1, 1] + [0 for _ in range(500)]


def factorial(n):
    if fact[n] != 0:
        return fact[n]
    if fact[n - 1] != 0:
        fact[n] = n * fact[n - 1]
        return fact[n]
    return n * factorial(n - 1)


n = int(sys.stdin.readline())
m = factorial(n)
p = list(str(m))
count = 0
for i in range(len(p) - 1, -1, -1):
    if p[i] == '0':
        count += 1
    else:
        break
print(count)