a = input()
b = input()
c = int(a) * int(str(b)[2])
d = int(a) * int(str(b)[1])
e = int(a) * int(str(b)[0])
print(c)
print(d)
print(e)
print(100 * e + 10 * d + c)