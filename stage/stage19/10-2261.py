import sys

n = int(sys.stdin.readline())
points = []
for _ in range(n):
    points.append(tuple(map(int, sys.stdin.readline().split())))
points = list(set(points))
points.sort(key=lambda x: x[0])


def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def divideandconquer(m):
    if len(m) == 2:
        return distance(m[0], m[1])
    elif len(m) == 3:
        return min(distance(m[0], m[1]), distance(m[0], m[2]), distance(m[1], m[2]))
    else:
        mid = len(m) // 2
        minimumd = min(divideandconquer(m[:mid]), divideandconquer(m[mid:]))
        temp = []
        for i in range(len(m)):
            if (m[i][0] - m[mid][0]) ** 2 <= minimumd:
                temp.append(m[i])
        if len(temp) >= 2:
            temp.sort(key=lambda x: x[1])
            for i in range(len(temp) - 1):
                for j in range(i + 1, len(temp)):
                    if (temp[i][1] - temp[j][1]) ** 2 > minimumd:
                        break
                    elif temp[i][0] < m[mid][0] and temp[j][0] < m[mid][0]:
                        continue
                    elif temp[i][0] >= m[mid][0] and temp[j][0] >= m[mid][0]:
                        continue
                    minimumd = min(minimumd, distance(temp[i], temp[j]))
        return minimumd


if n != len(points):
    print(0)
else:
    print(divideandconquer(points))
