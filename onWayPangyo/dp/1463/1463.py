import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

n = int(input())
cnt = 0
seta = set([n])
while 1 not in seta:
    setb = set()
    for i in seta:
        if i % 2 == 0:
            setb.add(i // 2)
        if i % 3 == 0:
            setb.add(i // 3)
        setb.add(i - 1)
    seta = set(setb)
    cnt += 1
print(cnt)
