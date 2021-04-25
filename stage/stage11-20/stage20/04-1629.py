a, b, c = map(int, input().split())
b2 = []
while b != 0:
    b2.append(b % 2)
    b //= 2
a2 = [a % c]
for i in range(1, len(b2)):
    a2.append(a2[i - 1] ** 2 % c)
ans = 1
for j in range(len(a2)):
    if b2[j] == 1:
        ans *= a2[j] * b2[j]
print(ans % c)