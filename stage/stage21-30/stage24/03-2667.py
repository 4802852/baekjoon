import sys

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
assigned = [[0 for _ in range(n)] for __ in range(n)]
cnt = 1
count = []


def dfs(x, y):
    global eachcnt
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    assigned[x][y] = cnt
    eachcnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1 and assigned[nx][ny] == 0:
            dfs(nx, ny)


for j in range(n):
    for k in range(n):
        if array[j][k] == 1 and assigned[j][k] == 0:
            eachcnt = 0
            dfs(j, k)
            count.append(eachcnt)
            cnt += 1
count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])