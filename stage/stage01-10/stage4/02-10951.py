import sys

while 1:
    n = sys.stdin.readline()
    try:
        a, b = map(int, n.split())
        print(a + b)
    except:
        break
