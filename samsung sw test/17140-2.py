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
    if row_val < col_val:
        # 열수 < 행수 조건일 경우 주어진 배열을 transpose 해주고 마지막에 다시 transpose 해줌으로써 코드를 간결히 하였다.
        matrix = list(zip(*matrix))
        next_row_val = col_val
    else:
        next_row_val = row_val
    new_matrix = []
    next_col_val = 0
    for i in range(len(matrix)):
        # 계산하는 행 또는 열을 탐색하여 {수: 해당 수의 개수} 형태로 저장하는 딕셔너리
        values = {}
        for n in matrix[i]:
            if n == 0:
                # 0은 카운트하지 않는다.
                continue
            if n not in values.keys():
                values[n] = 1
            else:
                values[n] += 1
        # 딕셔너리의 아이템들을 리스트로 만들고 문제에 주어진 조건에 맞추어 정렬해준다.
        tmp = list(values.items())
        tmp.sort(key=lambda x: x[0])
        tmp.sort(key=lambda x: x[1])
        values_to_list = []
        for a, b in tmp:
            values_to_list.append(a)
            values_to_list.append(b)
        new_matrix.append(values_to_list)
        # 리스트의 최대 길이를 저장하여 다음 행렬의 크기를 결정해준다.
        next_col_val = max(next_col_val, len(values_to_list))
    next_col_val = min(next_col_val, 100)
    matrix = [[0] * next_col_val for _ in range(next_row_val)]
    for i in range(next_row_val):
        max_j = min(100, len(new_matrix[i]))
        for j in range(max_j):
            matrix[i][j] = new_matrix[i][j]
    if row_val < col_val:
        # 처음에 transpose 해주었을 경우 이를 다시 transpose 해주어 되돌린다.
        matrix = list(zip(*matrix))
    return matrix


flag = 0
for i in range(101):
    try:
        # matrix[r][c] 배열 범위 바깥에 있을 경우 인덱스에러를 일으키므로 조건을 걸어준다.
        kk = matrix[r][c]
    except:
        kk = 0
    if kk == k:
        flag = 1
        break
    matrix = process(matrix)
if flag:
    print(i)
else:
    print(-1)
