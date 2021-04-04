import sys


move_count = []


def move(start, end, n):
    station = [1, 2, 3]
    station.remove(start)
    station.remove(end)
    mid = station[0]
    if n == 1:
        return move_count.append('{} {}'.format(start, end))
    move(start, mid, n - 1)
    move(start, end, 1)
    move(mid, end, n - 1)


n = int(input())
move(1, 3, n)
print(len(move_count))
for i in range(len(move_count)):
    print(move_count[i])