import sys


n, m = map(int, sys.stdin.readline().split())
c = [i for i in range(1, n + 1)]


def visit(c, m):
    ans = []
    if m == 0 or m > len(c):
        return ans
    elif m == 1:
        return list(map(lambda x: (x,), c))
    else:
        for i in range(len(c)):
            temp = c[i + 1:]
            ans += tuple(map(lambda x: (c[i],) + x, visit(temp, m - 1)))
    return ans


k = visit(c, m)
for i in range(len(k)):
    temp = map(lambda x: '{}'.format(x), list(k[i]))
    print(' '.join(temp))


# n, m = map(int, sys.stdin.readline().split())
# n_array = [i for i in range(1, n + 1)]
# a = [0] * n
# c = []
# while a != [1] * n:
#     a[-1] += 1
#     for i in range(len(a) - 1, -1, -1):
#         if a[i] == 2:
#             a[i] -= 2
#             a[i - 1] += 1
#     c.append(a[:])
# c.sort(reverse=True)
# d = []
# for i in range(len(c)):
#     if sum(c[i]) == m:
#         d.append(c[i])
# for i in range(len(d)):
#     ans = []
#     for j in range(len(d[i])):
#         if d[i][j] == 1:
#             ans.append(str(n_array[j]))
#     print(' '.join(ans))