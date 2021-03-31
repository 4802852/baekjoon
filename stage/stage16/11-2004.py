import sys


def c_two(n):
    count = 0
    while n != 0:
        n = n // 2
        count += n
    return count


def c_five(n):
    count = 0
    while n != 0:
        n = n // 5
        count += n
    return count


a, b = map(int, input().split())
if b == 0:
    print(0)
else:
    print(min(c_two(a) - c_two(b) - c_two(a - b), c_five(a) - c_five(b) - c_five(a - b)))


# sys.setrecursionlimit(10**6)
#
#
# fact = [1, 1] + [0 for _ in range(2000000000)]
#
#
# def factorial(n):
#     if fact[n] != 0:
#         return fact[n]
#     if fact[n - 1] != 0:
#         fact[n] = n * fact[n - 1]
#         return fact[n]
#     return n * factorial(n - 1)
#
#
# a, b = map(int, input().split())
# c = factorial(a)
# d = factorial(b)
# e = factorial(a - b)
# p = list(str(c // (d * e)))
# count = 0
# for i in range(len(p) - 1, -1, -1):
#     if p[i] == '0':
#         count += 1
#     else:
#         break
# print(count)