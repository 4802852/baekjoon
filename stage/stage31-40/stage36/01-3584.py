import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    parent = [0] * (n + 1)
    for __ in range(n - 1):
        p, c = map(int, sys.stdin.readline().split())
        parent[c] = p
    a, b = map(int, sys.stdin.readline().split())
    a_list = [0, a]
    b_list = [0, b]
    while parent[a]:
        a_list.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_list.append(parent[b])
        b = parent[b]
    cnt = 1
    while a_list[-cnt] == b_list[-cnt]:
        cnt += 1
    print(a_list[-cnt + 1])