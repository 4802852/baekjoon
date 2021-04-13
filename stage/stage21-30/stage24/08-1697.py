import sys

n, k = map(int, sys.stdin.readline().split())
location = [-1 for _ in range(100001)]
q = [n]
location[n] = 0
while q:
    now = q.pop(0)
    next = [now * 2, now + 1, now - 1]
    for i in range(3):
        if 0 <= next[i] <= 100000 and location[next[i]] == -1:
            location[next[i]] = location[now] + 1
            q.append(next[i])
    if location[k] != -1:
        break
print(location[k])