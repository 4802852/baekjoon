import sys


n = int(sys.stdin.readline())
triangle = [[0] * (n + 1) for _ in range(n)]
max_route = triangle[:]
for i in range(n):
    m = list(map(int, sys.stdin.readline().split()))
    for j in range(len(m)):
        triangle[i][j + 1] = m[j]
max_route[0] = triangle[0]
for k in range(1, n):
    for l in range(1, n + 1):
        max_route[k][l] = max(max_route[k - 1][l - 1], max_route[k - 1][l]) + triangle[k][l]
print(max(max_route[-1]))