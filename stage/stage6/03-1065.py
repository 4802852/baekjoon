count = 0
k = int(input())

def hannum(a):
    if len(str(a)) <= 2:
        return 1
    else:
        n = str(a)
        if (int(n[1]) - int(n[0])) == (int(n[2]) - int(n[1])):
            return 1
        return 0


for i in range(1, k + 1):
    count += hannum(i)
print(count)
