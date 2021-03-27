import sys

n = int(sys.stdin.readline())
max_stair = [[0, 0] for _ in range(n + 1)]  # 각 요소는 0번 요소로 두 칸 올라온 max, 1번 요소로 한 칸 올라온 max를 가진다.
stair = [0 for __ in range(n + 1)]
for i in range(1, n + 1):
    stair[i] = int(sys.stdin.readline())
max_stair[0] = [0, 0]
max_stair[1] = [stair[1], stair[1]]
if n > 1:
    for j in range(2, n + 1):
        max_stair[j][0] = max(max_stair[j - 2]) + stair[j]
        max_stair[j][1] = max_stair[j - 1][0] + stair[j]
print(max(max_stair[-1]))
