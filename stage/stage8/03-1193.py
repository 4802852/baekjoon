x = int(input())
n = 0
while x > 0:
    n += 1
    x -= n
x += n
a = n - x + 1
b = x
if n % 2 == 1:
    print('{}/{}'.format(a, b))
else:
    print('{}/{}'.format(b, a))

