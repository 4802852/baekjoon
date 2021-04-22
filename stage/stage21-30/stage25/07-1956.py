import sys

INF = float('inf')
v, e = map(int, sys.stdin.readline().split())
road = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    if road[a][b] > c:
        road[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if i != j and road[i][j] > road[i][k] + road[k][j]:
                road[i][j] = road[i][k] + road[k][j]

minimum = INF
for i in range(1, v):
    for j in range(i + 1, v + 1):
        minimum = min(minimum, road[i][j] + road[j][i])

# for k in range(1, v + 1):
#     for i in range(1, v + 1):
#         for j in range(1, v + 1):
#             if road[i][j] > road[i][k] + road[k][j]:
#                 road[i][j] = road[i][k] + road[k][j]
# 
# minimum = INF
# for i in range(1, v + 1):
#     minimum = min(minimum, road[i][i])

print(-1 if minimum == INF else minimum)



