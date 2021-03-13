c = []


def kaprekar(a: int) -> int:
    if a < 10001:
        n = len(str(a))
        b = str(a)
        for i in range(n):
            a += int(b[i])
        c.append(a)
        kaprekar(a)
    else:
        return c


k = []
for i in range(1, 10001):
    k.append(i)

for i in range(1, 10001):
    kaprekar(i)

e = set(c)
c = list(e)
c.sort()

d = [item for item in k if item not in c]

for i in d:
    print(i)

