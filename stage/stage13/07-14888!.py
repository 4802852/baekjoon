# python으로 시간초과 계속되어 pypy3으로 통과. 최적화 더 할게 남아있는지..?

import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
a, b, c, d = map(int, sys.stdin.readline().split())
cal_list = ['p' for i in range(a)] + ['m' for j in range(b)] + ['u' for k in range(c)] + ['d' for l in range(d)]
cal_used = [False for x in range(len(cal_list))]
ans = []
temp = [number_list[0]]


def calculate(e, g, f):
    if g == 'p':
        return e + f
    elif g == 'm':
        return e - f
    elif g == 'u':
        return e * f
    else:
        if e * f < 0:
            return -((-e) // f)
        return e // f


def mix(x):
    if x == len(cal_list):
        ans.append(temp[x])
        return
    for i in range(len(cal_list)):
        if cal_used[i]:
            continue
        cal_used[i] = True
        result = calculate(temp[x], cal_list[i], number_list[x + 1])
        temp.append(result)
        mix(x + 1)
        temp.pop()
        cal_used[i] = False


mix(0)
print(max(ans))
print(min(ans))
