import sys


n = int(sys.stdin.readline())
price = [[0, 0, 0]]
for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    price.append([r, g, b])
min_price = []
min_price.append([0, 0, 0])
for j in range(1, n + 1):
    temp0 = min(min_price[j - 1][1], min_price[j - 1][2]) + price[j][0]
    temp1 = min(min_price[j - 1][0], min_price[j - 1][2]) + price[j][1]
    temp2 = min(min_price[j - 1][0], min_price[j - 1][1]) + price[j][2]
    min_price.append([temp0, temp1, temp2])
print(min(min_price[n]))


# prev = []
# price2 = []
# price_sum_list = []
#
#
# def select(previous, a):
#     if a == n:
#         price_sum_list.append(sum(price2))
#         return
#     for j in range(3):
#         if j == previous:
#             continue
#         price2.append(price[a][j])
#         prev.append(j)
#         select(prev[-1], a + 1)
#         prev.pop()
#         price2.pop()
#
#
# select(-1, 0)
# print(min(price_sum_list))
