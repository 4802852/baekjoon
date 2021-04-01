from collections import deque

n = int(input())
q = deque([i for i in range(1, n + 1)])
if n > 1:
    q.popleft()
while len(q) > 1:
    q.append(q.popleft())
    q.popleft()
print(q[0])