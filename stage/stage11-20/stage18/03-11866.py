from collections import deque

a, b = map(int, input().split())
q = deque([i for i in range(1, a + 1)])
y = []
while len(q) > 0:
    for i in range(b):
        if i == b - 1:
            y.append(q.popleft())
        else:
            q.append(q.popleft())
print('<', end='')
for j in y:
    if j == y[-1]:
        print(j, end='')
    else:
        print(j, end=', ')
print('>')