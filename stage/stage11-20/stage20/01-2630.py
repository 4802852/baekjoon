import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
count = [0, 0]  # 하얀색, 파란색


def cut(x, y, n):
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return
    if check == 0:
        count[0] += 1
        return
    else:
        count[1] += 1
        return


cut(0, 0, n)
print(count[0])
print(count[1])