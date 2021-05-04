import sys


def ismap(x, y):  # 해당 좌표가 지도 안에 있는지 판단해주는 함수
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


n, m = map(int, sys.stdin.readline().split())
mapArr = []  # 지도 Array
for _ in range(n):
    mapArr.append(list(map(int, sys.stdin.readline().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
boundary = [[] for _ in range(8)]  # boundary[i]: i 섬의 외곽 좌표, 다리의 시작점 탐색 때 사용


def labeling(x, label):  # mapArr x 좌표에서 시작하여 연결된 땅들을 label 숫자로 바꾸어주는 함수
    q = [x]
    mapArr[x[0]][x[1]] = label
    tmpBoundary = []  # label 되고 있는 섬의 외곽 좌표들을 저장해주는 임시 list
    while q:
        now = q.pop(0)
        boundaryCheck = False
        for k in range(4):
            nx, ny = now[0] + dx[k], now[1] + dy[k]
            if ismap(nx, ny):
                if mapArr[nx][ny] == 1:
                    mapArr[nx][ny] = label
                    q.append([nx, ny])
                elif mapArr[nx][ny] == 0:  # now 좌표를 기준으로 주변에 0, 즉 바다가 있으면 외곽 좌표 표시
                    boundaryCheck = True
        if boundaryCheck:
            tmpBoundary.append([now[0], now[1]])
    boundary[label] = tmpBoundary


label = 2  # 주어진 지도에 땅이 1로 표시되어 있으므로 섬을 2부터 라벨링
for i in range(n):
    for j in range(m):
        if mapArr[i][j] == 1:
            labeling([i, j], label)
            label += 1
# 이 과정 후에 label 은 마지막 라벨링된 섬이 가진 수 +1 의 값을 가짐
bridges = [[0] * label for _ in range(label)]  # bridges[i][j]: i 섬에서 j 섬까지 연결하는 다리의 길이

for now in range(2, label):  # 각 섬들을 탐색
    for x, y in boundary[now]:  # 각 섬들의 외곽 좌표를 탐색
        for k in range(4):  # 각 섬들의 외곽에서 4방향으로 탐색하여 지도 밖으로 나가거나, 다른 섬을 만날때까지 탐색
            nx, ny = x + dx[k], y + dy[k]
            if ismap(nx, ny):
                cnt = 0
                while mapArr[nx][ny] == 0:
                    cnt += 1
                    nx += dx[k]
                    ny += dy[k]
                    if not ismap(nx, ny):
                        cnt = 0
                        break
                if cnt >= 2:  # 다리가 진행하다가 다른 섬을 만났을 경우 해당 섬과의 bridges 리스트를 갱신
                    if bridges[now][mapArr[nx][ny]]:
                        bridges[now][mapArr[nx][ny]] = min(bridges[now][mapArr[nx][ny]], cnt)
                        bridges[mapArr[nx][ny]][now] = bridges[now][mapArr[nx][ny]]
                    else:
                        bridges[now][mapArr[nx][ny]] = cnt
                        bridges[mapArr[nx][ny]][now] = cnt

lines = []
for i in range(2, label):
    for j in range(i + 1, label):
        if bridges[i][j]:
            lines.append([bridges[i][j], i, j])  # i 에서 j 로 가는 다리의 길이가 bridges[i][j]
# 이 과정을 거친 후에는 보통의 유니온파인드 문제들과 같이 풀이
parent = [i for i in range(label)]
lines.sort()


def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    parent[y] = x


cnt2 = 0
ans = 0
for co in lines:
    d, a, b = co
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        ans += d
        cnt2 += 1
    if cnt2 == label - 3:
        break
if cnt2 != label - 3:  # 모든 다리들의 탐색이 끝났는데 다리의 수가 섬의 개수 - 1 개가 되지 않으면
    print(-1)  # 연결되지 않은 섬이 존재
else:
    print(ans)  # 그렇지 않으면 다리의 총 길이 출력
