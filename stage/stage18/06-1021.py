from collections import deque

a, b = map(int, input().split())
dq = deque([0 for _ in range(a)])
m = list(map(int, input().split()))
for i in range(b):
    dq[m[i] - 1] = i + 1
count = 0
for i in range(1, b + 1):
    # i len(dq) - i
    k = dq.index(i)
    if k <= len(dq) - k:
        for _ in range(k):
            dq.append(dq.popleft())
            count += 1
    else:
        for _ in range(len(dq) - k):
            dq.appendleft(dq.pop())
            count += 1
    dq.popleft()
print(count)