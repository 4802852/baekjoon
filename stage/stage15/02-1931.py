import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    s.append([start, end])
s.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = s[0][1]
for i in range(1, n):
    if s[i][0] >= end_time:
        cnt += 1
        end_time = s[i][1]
print(cnt)
