import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rc = [0, 0, -1, 1]
cc = [1, -1, 0, 0]
# (r, c) 위치에 몇 번 말들이 어떤 순서로 쌓여있는지를 저장해주는 matrix 행렬
matrix = [[[] for _ in range(N)] for _ in range(N)]
# n번 말이 어떤 위치와 어떤 방향 정보를 가지고 있는지를 [r, c, d] 형식으로 저장하는 pieces 리스트
pieces = []
for i in range(K):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    matrix[r][c].append(i)
    pieces.append([r, c, d])


def move(move_list):
    # n번 말을 이동할 때 해당 말과 그 위에 쌓여 있는 말들의 리스트인 move_list를 입력으로 받는다.
    # 이동할 말의 위치 및 방향 정보를 확인한다.
    r, c, d = pieces[move_list[0]]
    # 이미 가지고 있는 방향에서의 새로운 위치
    nr, nc = r + rc[d], c + cc[d]
    if nr < 0 or N <= nr or nc < 0 or N <= nc or board[nr][nc] == 2:
        # 새로운 위치가 지도 바깥으로 나가거나 파란색(값이 2) 일 경우, 방향을 반대로 바꿔준다.
        if d == 0 or d == 2:
            d += 1
        else:
            d -= 1
        nr, nc = r + rc[d], c + cc[d]
        if nr < 0 or N <= nr or nc < 0 or N <= nc or board[nr][nc] == 2:
            # 방향이 바뀐 후 이동한 칸이 여전히 지도 바깥이거나 파란색일 경우 이동하지 않고 결과를 리턴해준다.
            return [r, c, d, move_list]
    if board[nr][nc] == 1:
        # 이동한 위치의 색이 빨간색일 경우 move_list를 거꾸로 바꿔준다.
        tmp_list = []
        while move_list:
            tmp_list.append(move_list.pop())
        move_list = tmp_list
    # 새로운 위치인 nr, nc와 바뀐 방향인 d, 그리고 같이 이동하게 되는 말들의 리스트를 리턴한다.
    return [nr, nc, d, move_list]


def process():
    # K개의 말을 순차적으로 탐색한다.
    for n in range(K):
        # n번 말의 위치 (r, c)를 확인하여 n번말을 포함하여 위로 쌓여있는 말들의 리스트인 list_to_move를 찾는다.
        r, c, d = pieces[n]
        n_index = matrix[r][c].index(n)
        list_to_move = matrix[r][c][n_index:]
        matrix[r][c] = matrix[r][c][:n_index]
        nr, nc, nd, list_to_move = move(list_to_move)
        matrix[nr][nc] += list_to_move
        # 이동한 말들의 위치를 pieces 리스트에 갱신해준다.
        for nn in list_to_move:
            if nn == n:
                pieces[nn] = [nr, nc, nd]
            else:
                pieces[nn][0] = nr
                pieces[nn][1] = nc
        if len(matrix[nr][nc]) >= 4:
            # 새로운 위치에 말이 4개 이상 있을 경우 1을 리턴
            return 1
    # 정상적으로 모든 이동이 이루어지면 0 리턴
    return 0


flag = 0
for i in range(1000):
    flag = process()
    if flag:
        # 1이 리턴되었을 경우 어느 한 위치에 말이 4개 이상 쌓였다는 의미.
        break
if flag:
    print(i + 1)
else:
    print(-1)
