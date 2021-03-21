import sys


n, m = map(int, sys.stdin.readline().split())
c = [i for i in range(1, n + 1)]


def visit(c, m):
    ans = []
    if m == 0:
        return ans
    elif m == 1:
        return list(map(lambda x: (x,), c))
    else:
        for i in range(len(c)):
            temp = []
            temp += c[i:]
            ans += tuple(map(lambda x: (c[i],) + x, visit(temp, m - 1)))
    return ans


k = visit(c, m)
for i in range(len(k)):
    temp = map(lambda x: '{}'.format(x), list(k[i]))
    print(' '.join(temp))