n = int(input())

bag = 0
not_good = [4, 7]

if n in not_good:
    print(-1)
else:
    if n % 5 == 0:
        bag = n // 5
    elif n % 5 == 1:
        bag = n // 5 - 1 + 2
    elif n % 5 == 2:
        bag = n // 5 - 2 + 4
    elif n % 5 == 3:
        bag = n // 5 + 1
    else:
        bag = n // 5 - 1 + 3
    print(bag)