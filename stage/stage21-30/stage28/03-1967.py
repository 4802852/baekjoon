import sys

sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append([b, c])
    tree[b].append([a, c])


def dfs(start, result):
    for e, d in tree[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            dfs(e, result)


result1 = [0 for _ in range(n + 1)]
dfs(1, result1)
result1[1] = 0
tmpmax = 0
tmpindex = 0
for i, x in enumerate(result1):
    if tmpmax < x:
        tmpmax = x
        tmpindex = i

result2 = [0 for _ in range(n + 1)]
dfs(tmpindex, result2)
result2[tmpindex] = 0
print(max(result2))