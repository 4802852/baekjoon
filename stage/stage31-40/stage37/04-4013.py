import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
# 코사라주 SCC 탐색을 위한 정방향/역방향 그래프
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    reverse_graph[b].append(a)
# ATM 에 있는 금액 저장
atm = [0] * (n + 1)
for i in range(1, n + 1):
    atm[i] = int(sys.stdin.readline())
# 시작점 및 레스토랑 위치 저장
s, p = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
restaurant = [0] * (n + 1)
for i in tmp:
    restaurant[i] = 1


def dfs(x, visited, stack):
    visited[x] = 1
    for ne in graph[x]:
        if visited[ne] == 0:
            dfs(ne, visited, stack)
    stack.append(x)


def reverse_dfs(x, visited, scc):
    global idid
    visited[x] = 1
    ids[x] = idid
    scc.append(x)
    for ne in reverse_graph[x]:
        if visited[ne] == 0:
            reverse_dfs(ne, visited, scc)


stack = []
visited = [0] * (n + 1)
for j in range(1, n + 1):
    if visited[j] == 0:
        dfs(j, visited, stack)
visited = [0] * (n + 1)
idid = 0
ids = [-1] * (n + 1)
result = [[] for _ in range(n + 1)]
while stack:
    scc = []
    node = stack.pop()
    if visited[node] == 0:
        idid += 1
        reverse_dfs(node, visited, scc)
        result[idid] = scc

# 코사라주 알고리즘으로 묶은 scc 를 이용, scc 를 한개의 node 로 보고 새로운 graph, atm, restaurant 작성
graph2 = [[] for _ in range(idid + 1)]
for i in range(1, n + 1):
    for j in graph[i]:
        if ids[i] != ids[j]:
            graph2[ids[i]].append(ids[j])
atm2 = [0] * (idid + 1)
restaurant2 = [0] * (idid + 1)
for i in range(1, idid + 1):
    for j in result[i]:
        atm2[i] += atm[j]
        restaurant2[i] += restaurant[j]
# 새로운 graph, atm, restaurant 이용하여 시작점으로부터 dfs 탐색
visited = [0] * (idid + 1)
tmp = 0
maximum = 0


def restaurant_dfs(x):
    global tmp, maximum
    visited[x] = 1
    tmp += atm2[x]
    # 해당 위치 혹은 scc 에 레스토랑 있을 경우 maximum 값 갱신
    if restaurant2[x] >= 1:
        maximum = max(maximum, tmp)
    for ne in graph2[x]:
        if visited[ne] == 0:
            restaurant_dfs(ne)
    tmp -= atm2[x]


restaurant_dfs(ids[s])
print(maximum)
