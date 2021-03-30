m, n = map(int, input().split())
if m % n == 0:
    min_m = n
    max_m = m
elif n % m == 0:
    min_m = m
    max_m = n
else:
    i = 0
    a = min(m, n) // 2
    while 1:
        if m % a == 0 and n % a == 0:
            min_m = a
            break
        a -= 1
    max_m = (m // a) * n
print('{} {}'.format(min_m, max_m))