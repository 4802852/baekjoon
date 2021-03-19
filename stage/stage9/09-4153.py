import sys


while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if [a, b, c] == [0, 0, 0]:
        break
    t = [a, b, c]
    l = max(t)
    t.remove(l)
    if l**2 == t[0]**2 + t[1]**2:
        print('right')
    else:
        print('wrong')