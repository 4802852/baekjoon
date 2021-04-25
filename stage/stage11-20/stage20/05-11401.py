import sys

n, k = map(int, sys.stdin.readline().split())
c = 1000000007


def power(a, b):
    b2 = []
    while b != 0:
        b2.append(b % 2)
        b //= 2
    a2 = [a % c]
    for i in range(1, len(b2)):
        a2.append(a2[i - 1] ** 2 % c)
    ans = 1
    for j in range(len(a2)):
        if b2[j] == 1:
            ans *= a2[j] * b2[j]
    return ans % c


fact = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % c

a = fact[n]
b = (fact[n - k] * fact[k]) % c
print((a % c) * (power(b, c - 2) % c) % c)
