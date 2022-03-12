import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

r, c, k = map(int, input().split())
r -= 1
c -= 1
matrix = [list(map(int, input().split())) for _ in range(3)]
t = 0


def process(matrix):
    row_val = len(matrix)
    col_val = len(matrix[0])
    if row_val >= col_val:
        new_matrix = []
        cnt_max = 0
        for i in range(row_val):
            tmp = [float("inf")] * 101
            for n in matrix[i]:
                if tmp[n] == float("inf"):
                    tmp[n] = 0
                tmp[n] += 1
            cnt = 0
            tmp_arr = []
            while min(tmp) != float("inf"):
                val = tmp.index(min(tmp))
                if val == 0:
                    tmp[val] = float("inf")
                    continue
                tmp_arr.append(val)
                tmp_arr.append(tmp[val])
                tmp[val] = float("inf")
                cnt += 1
            cnt_max = max(cnt_max, cnt)
            new_matrix.append(tmp_arr)
        matrix = [[0] * min(100, cnt_max * 2) for _ in range(row_val)]
        for i in range(row_val):
            max_j = min(len(new_matrix[i]), 100)
            for j in range(max_j):
                matrix[i][j] = new_matrix[i][j]
    else:
        new_matrix = []
        cnt_max = 0
        for i in range(col_val):
            tmp = [float("inf")] * 101
            for j in range(row_val):
                if tmp[matrix[j][i]] == float("inf"):
                    tmp[matrix[j][i]] = 0
                tmp[matrix[j][i]] += 1
            cnt = 0
            tmp_arr = []
            while min(tmp) != float("inf"):
                val = tmp.index(min(tmp))
                if val == 0:
                    tmp[val] = float("inf")
                    continue
                tmp_arr.append(val)
                tmp_arr.append(tmp[val])
                tmp[val] = float("inf")
                cnt += 1
            cnt_max = max(cnt_max, cnt)
            new_matrix.append(tmp_arr)
        matrix = [[0] * col_val for _ in range(min(100, cnt_max * 2))]
        for i in range(col_val):
            max_j = min(len(new_matrix[i]), 100)
            for j in range(max_j):
                matrix[j][i] = new_matrix[i][j]
    return matrix


try:
    flag = matrix[r][c]
except:
    flag = 0
while flag != k:
    matrix = process(matrix)
    t += 1
    try:
        flag = matrix[r][c]
    except:
        flag = 0
    if t == 101:
        break
if t == 101:
    print(-1)
else:
    print(t)
