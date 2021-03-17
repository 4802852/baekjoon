import sys


# def num(k, n):
#     # if k == 0:
#     #     return floor[0][n - 1]
#     # if n == 1:
#     #     return 1
#     # return sum([num(k - 1, i) for i in range(1, n + 1)])
#     # return num(k - 1, n) + num(k, n - 1)
#     for i in range(1, k + 1):
#         floor.append([])
#         # print(floor)
#         for j in range(n):
#             if j == 0:
#                 floor[i].append(1)
#                 # print(floor)
#             else:
#                 floor[i].append(floor[i][j - 1] + floor[i - 1][j])
#                 # print(floor)
#     return sum(floor[k - 1][:n])

def num(k, n):
    if k == 1:
        return sum(floor[0][:n])
    for i in range(1, k):
        floor.append([])
        for j in range(n):
            if j == 0:
                floor[i].append(1)
            else:
                floor[i].append(floor[i][j - 1] + floor[i - 1][j])
    return sum(floor[k - 1][:n])


t = int(sys.stdin.readline())
for i in range(t):
    floor = [[i for i in range(1, 15)]]
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(num(k, n))



