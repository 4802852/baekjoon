n = int(input())
num = [0, 1, 2]
if n > 2:
    num = num + [0] * (n - 2)
    for i in range(3, n + 1):
        num[i] = (num[i - 1] + num[i - 2]) % 15746
print(num[n])