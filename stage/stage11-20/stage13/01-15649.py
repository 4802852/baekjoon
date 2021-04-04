import sys


n, m = map(int, sys.stdin.readline().split())
c = [i for i in range(1, n + 1)]


def visit(d, m):
    ans = []
    if m == 0 or m > len(d):
        return ans
    elif m == 1:
        return list(map(lambda x: (x,), d))
    else:
        for i in range(len(d)):
            temp = d[:]
            temp.remove(d[i])
            ans += tuple(map(lambda x: (d[i],) + x, visit(temp, m - 1)))
    return ans


k = visit(c, m)
for i in range(len(k)):
    temp = map(lambda x: '{}'.format(x), list(k[i]))
    print(' '.join(temp))