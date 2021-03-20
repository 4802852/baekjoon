import sys


def star(size):
    if size == 3:
        return [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
    ans = [[0] * size for i in range(size)]
    temp = star(size // 3)
    for i in range(size):
        for j in range(size):
            if i // (size // 3) == j // (size // 3) == 1:
                ans[i][j] = ' '
            else:
                ans[i][j] = temp[i % (size // 3)][j % (size // 3)]
    return ans


n = int(input())
a = star(n)
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print(end='\n')
