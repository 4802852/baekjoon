import sys


# def bfs(x):
#     q = [x]
#     visited[x] = 1
#     cnt = 0
#     while q:
#         now = q.pop(0)
#         for nx in air[now]:
#             if visited[nx] == 0:
#                 visited[nx] = 1
#                 cnt += 1
#                 q.append(nx)
#     return cnt


for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    # air = [[] for __ in range(n + 1)]
    # visited = [0 for __ in range(n + 1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
    #     air[a].append(b)
    #     air[b].append(a)
    # ans = 0
    # for i in range(1, n + 1):
    #     if visited[i] == 0:
    #         ans += bfs(i)
    # print(ans)
    print(n - 1)
