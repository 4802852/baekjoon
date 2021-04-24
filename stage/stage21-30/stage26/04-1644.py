import sys

n = int(sys.stdin.readline())


def prime(n):
    primes = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if primes[i] is True:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(2, n) if primes[i] is True]


if n >= 2:
    primes = prime(n + 1)
    left, right = 0, 0
    tmp = primes[left]
    cnt = 0
    while left <= right:
        if tmp < n:
            right += 1
            if right == len(primes):
                break
            tmp += primes[right]
        elif tmp > n:
            tmp -= primes[left]
            left += 1
        else:
            cnt += 1
            tmp -= primes[left]
            left += 1
else:  # n = 1 일 때, 1은 소수가 아니므로 0이다.
    cnt = 0
print(cnt)