import sys
from math import pi, atan2

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())

d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
if d >= r1 + r2:
    ans = 0
if d <= abs(r1 - r2):
    ans = pi * (min(r1, r2) ** 2)
if max(r1, r2) - min(r1, r2) < d < r1 + r2:
    x = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    y = (r1 ** 2 - x ** 2) ** 0.5
    theta1 = atan2(y, x) / pi * 180
    theta2 = atan2(y, d - x) / pi * 180
    ans = pi * (r1 ** 2) * theta1 / 180 + pi * (r2 ** 2) * theta2 / 180 - d * y
print('%.3f' % ans)
