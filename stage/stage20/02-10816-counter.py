import sys
from collections import Counter

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()

counter = Counter(a)

print(' '.join(str(counter[c]) if c in counter else '0' for c in b))