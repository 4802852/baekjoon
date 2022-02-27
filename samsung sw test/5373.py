import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사


def turn_face(face, direction):
    if direction == 1:
        tmp1, tmp2 = cube[face][0][0], cube[face][0][1]
        cube[face][0][0], cube[face][0][1] = cube[face][2][0], cube[face][1][0]
        cube[face][2][0], cube[face][1][0] = cube[face][2][2], cube[face][2][1]
        cube[face][2][2], cube[face][2][1] = cube[face][0][2], cube[face][1][2]
        cube[face][0][2], cube[face][1][2] = tmp1, tmp2
    elif direction == -1:
        tmp1, tmp2 = cube[face][0][0], cube[face][0][1]
        cube[face][0][0], cube[face][0][1] = cube[face][0][2], cube[face][1][2]
        cube[face][0][2], cube[face][1][2] = cube[face][2][2], cube[face][2][1]
        cube[face][2][2], cube[face][2][1] = cube[face][2][0], cube[face][1][0]
        cube[face][2][0], cube[face][1][0] = tmp1, tmp2


def turn_cube(direction):
    if direction == 1:
        tmp1, tmp2, tmp3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[2][0][2], cube[2][0][1], cube[2][0][0]
        cube[2][0][2], cube[2][0][1], cube[2][0][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = tmp1, tmp2, tmp3
        turn_face(1, 1)
    elif direction == -1:
        tmp1, tmp2, tmp3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][0][2], cube[2][0][1], cube[2][0][0]
        cube[2][0][2], cube[2][0][1], cube[2][0][0] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = tmp1, tmp2, tmp3
        turn_face(1, -1)


def move_up():
    tmp_face = cube[0]
    cube[0] = cube[1]
    cube[1] = cube[2]
    cube[2] = cube[3]
    cube[3] = tmp_face
    turn_face(4, -1)
    turn_face(5, 1)


def move_down():
    tmp_face = cube[0]
    cube[0] = cube[3]
    cube[3] = cube[2]
    cube[2] = cube[1]
    cube[1] = tmp_face
    turn_face(4, 1)
    turn_face(5, -1)


def move_right():
    tmp_face = cube[5]
    cube[5] = cube[1]
    cube[1] = cube[4]
    cube[4] = cube[3]
    turn_face(4, 1)
    turn_face(4, 1)
    cube[3] = tmp_face
    turn_face(3, 1)
    turn_face(3, 1)
    turn_face(0, -1)
    turn_face(2, 1)


def move_left():
    tmp_face = cube[4]
    cube[4] = cube[1]
    cube[1] = cube[5]
    cube[5] = cube[3]
    turn_face(5, 1)
    turn_face(5, 1)
    cube[3] = tmp_face
    turn_face(3, 1)
    turn_face(3, 1)
    turn_face(0, 1)
    turn_face(2, -1)


def cubing(face, direction):
    if direction == "+":
        d = 1
    elif direction == "-":
        d = -1
    if face == "F":
        turn_cube(d)
    elif face == "B":
        move_up()
        move_up()
        turn_cube(d)
        move_down()
        move_down()
    elif face == "U":
        move_down()
        turn_cube(d)
        move_up()
    elif face == "D":
        move_up()
        turn_cube(d)
        move_down()
    elif face == "L":
        move_right()
        turn_cube(d)
        move_left()
    elif face == "R":
        move_left()
        turn_cube(d)
        move_right()


T = int(input())
for _ in range(T):
    # 0:윗면, 1:앞면, 2:아랫면, 3:밑면, 4:왼쪽면, 5:오른쪽면
    color = ["w", "r", "y", "o", "g", "b"]
    cube = []
    for i in range(6):
        tmp = [[color[i]] * 3 for _ in range(3)]
        cube.append(tmp)
    N = int(input())
    tmp = list(map(str, input().split()))
    for i in range(N):
        now = tmp[i]
        cubing(now[0], now[1])
    for line in cube[0]:
        for value in line:
            print(value, end="")
        print()
