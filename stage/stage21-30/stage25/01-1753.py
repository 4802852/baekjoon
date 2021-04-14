import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
lines = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    lines[a].append([c, b])
visited = [float('inf') for _ in range(v + 1)]
visited[start] = 0
heap = []
heapq.heappush(heap, (0, start))


def Dijkstara():
    while heap:
        weight, now = heapq.heappop(heap)
        if visited[now] < weight:
            continue
        for w, n in lines[now]:
            nw = w + weight
            if nw < visited[n]:
                visited[n] = nw
                heapq.heappush(heap, (nw, n))


Dijkstara()
# q = [start]
#
#
# def bfs():
#     while q:
#         now = q.pop(0)
#         temp = sorted(lines[now], key=lambda x: x[1])
#         for i in range(len(temp)):
#             if visited[temp[i][0]] > visited[now] + temp[i][1]:
#                 visited[temp[i][0]] = visited[now] + temp[i][1]
#                 q.append(temp[i][0])
#
#
# bfs()
for i in range(1, v + 1):
    if visited[i] == float('inf'):
        print('INF')
    else:
        print(visited[i])

