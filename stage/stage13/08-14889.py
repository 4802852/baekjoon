import sys


n = int(sys.stdin.readline())
table = []
for i in range(n):
    m = list(map(int, sys.stdin.readline().split()))
    table.append(m)
team_pool = set(range(1, n))
pool_used = [False] * n
pool_used[0] = True
team_start = [0]
team_start_possible = []
ans = []
score = [0, 0]


def team_making(x):
    if len(team_start) == n // 2:
        team_start_possible.append(set(team_start))
        return
    for j in range(x + 1, n):
        if pool_used[j] is True:
            continue
        team_start.append(j)
        pool_used[j] = True
        team_making(j)
        pool_used[j] = False
        team_start.pop()


team_making(0)
# print(team_start_possible)
for k in range(len(team_start_possible)):
    team_link = team_pool - team_start_possible[k]
    team_start_list = list(team_start_possible[k])
    team_link_list = list(team_link)
    for x in range(n // 2):
        for y in range(n // 2):
            score[0] += table[team_start_list[x]][team_start_list[y]] + table[team_start_list[y]][team_start_list[x]]
            score[1] += table[team_link_list[x]][team_link_list[y]] + table[team_link_list[y]][team_link_list[x]]
    # print(team_start_list, team_link_list, score)
    ans.append(abs(score[0] - score[1]) // 2)
    score = [0, 0]
print(min(ans))


# n = int(sys.stdin.readline())
# table = []
# for i in range(n):
#     m = list(map(int, sys.stdin.readline().split()))
#     table.append(m)
# pool = [i for i in range(n)]
# chosen = [False for i in range(n)]
#
# a = []
# b = []
# score = [0, 0]
# score_min = []
#
#
# def synergy(z):
#     if z == n / 2:
#         score_min.append(abs(score[0] - score[1]))
#         return
#     for d in range(len(pool)):
#         if chosen[d] is True:
#             continue
#         chosen[d] = True
#         a.append(d)
#         for j in range(len(a)):
#             score[0] += table[a[j]][d] + table[d][a[j]]
#         for e in range(len(pool)):
#             if chosen[e] is True:
#                 continue
#             b.append(e)
#             chosen[e] = True
#             for k in range(len(b)):
#                 score[1] += table[b[k]][e] + table[e][b[k]]
#             synergy(z + 1)
#             b.pop()
#             chosen[e] = False
#             for k in range(len(b)):
#                 score[1] -= table[b[k]][e] + table[e][b[k]]
#         a.pop()
#         chosen[d] = False
#         for j in range(len(a)):
#             score[0] -= table[a[j]][d] + table[d][a[j]]
#
#
# synergy(0)
# print(min(score_min))
