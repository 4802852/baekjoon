# n = int(input())
# # count = 0
# count = n
# for i in range(n):
#     # a = input()
#     # a = 'happy'
#     # group_word = True
#     stra = list(input())
#     now = stra.pop()
#     # print('now is ' + now)
#     while stra:
#         new = stra.pop()
#         # print('new is ' + new)
#         # print(stra)
#         if now == new:
#             pass
#         else:
#             if '{}'.format(now) in stra:
#                 # group_word = False
#                 count -= 1
#                 stra = []
#             else:
#                 new = now
#
#     # if group_word is True:
#     #     count += 1
#
# print(count)


n = int(input())
count = n
for i in range(n):
    stra = list(input())
    now = stra.pop()
    while stra:
        new = stra.pop()
        if now != new:
            if '{}'.format(now) in stra:
                count -= 1
                stra = []
            else:
                now = new

print(count)
