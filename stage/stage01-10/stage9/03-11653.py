import sys


# max = 10000
# k = list(range(2, max + 1))
# m = k[:]
# a = 0
# b = m[a]
# while m[a] != k[-1]:
#     a += 1
#     for i in range(a, len(k)):
#         if k[i] % b == 0:
#             m.remove(k[i])
#     b = m[a]
#     k = m[:]


# n = int(sys.stdin.readline())
# th = 0
# while n != 1:
#     if n % k[th] == 0:
#         print(k[th])
#         n = n / k[th]
#     else:
#         th += 1

n = int(sys.stdin.readline())
th = 2
while n != 1:
    if n % th == 0:
        print(th)
        n = n / th
    else:
        th += 1