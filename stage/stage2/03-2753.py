a = int(input())
n = 0
if a % 4 == 0:
    n += 1
if a % 100 == 0:
    n -= 1
if a % 400 == 0:
    n += 1
print(n)