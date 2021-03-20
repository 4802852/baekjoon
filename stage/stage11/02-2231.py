import sys


n = int(sys.stdin.readline())
start = n - int(len(str(n))) * 10
if start <= 1:
    start = 0
result = 0
while result != n:
    start += 1
    result = 0
    for i in range(len(str(start))):
        result += int(str(start)[i])
    result += start
    if start == n + 1:
        break

if start == n + 1:
    print(0)
else:
    print(start)