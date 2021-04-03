import sys

while 1:
    n, *temp = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        break
    histogram = [0] + temp + [0]
    checked = [0]
    area = 0

    for i in range(1, n + 2):
        while checked and histogram[checked[-1]] > histogram[i]:
            current = checked.pop()
            area = max(area, (i - 1 - checked[-1]) * histogram[current])
        checked.append(i)
    print(area)