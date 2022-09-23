import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
import heapq

input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split(" "))
    graph[a].append((d, b))
    graph[b].append((d, a))


# 달빛 여우: 일반적인 다익스트라 알고리즘
def dijkstra_fox():
    d = [INF] * (N + 1)
    d[1] = 0
    pq = [(0, 1)]
    while pq:
        weight, now = heapq.heappop(pq)
        if d[now] < weight:
            continue
        for w, n in graph[now]:
            nw = weight + w
            if nw < d[n]:
                d[n] = nw
                heapq.heappush(pq, (nw, n))
    return d


# 달빛 늑대: 달리기/걷기에 따른 가중치를 준 다익스트라 알고리즘
def dijkstra_wolf():
    # (N + 1) * 2 배열로 초기화
    d = [[INF] * 2 for _ in range(N + 1)]
    # 1번 위치에서 달려서(1) 출발한다는 의미
    d[1][1] = 0
    pq = [(0, 1, 1)]
    while pq:
        weight, now, run = heapq.heappop(pq)
        if d[now][run] < weight:
            continue
        for w, n in graph[now]:
            # now 위치에서 달려야 한다면(run == 1)
            if run:
                # 다음 위치로 갈 때 거리가 절반이라고 계산
                nw = weight + w / 2
                if nw < d[n][0]:
                    d[n][0] = nw
                    # 다음 위치 n 에서는 걸어서 출발하도록 run == 0 전달
                    heapq.heappush(pq, (nw, n, 0))
            # now 위치에서 걸어야 한다면(run == 0)
            else:
                # 다음 위치로 갈 때 거리가 두배라고 계산
                nw = weight + w * 2
                if nw < d[n][1]:
                    d[n][1] = nw
                    # 다음 위치에서는 뛰어서 출발하도록 run == 1 전달
                    heapq.heappush(pq, (nw, n, 1))
    return d


fox_d = dijkstra_fox()
wolf_d = dijkstra_wolf()
cnt = 0
# 달빛 여우가 n번 그루터기에서 걸린 시간이 달빛 늑대가 걸린 시간 2개보다 작다면 카운트
for i in range(1, N + 1):
    if fox_d[i] < wolf_d[i][0] and fox_d[i] < wolf_d[i][1]:
        cnt += 1
print(cnt)
