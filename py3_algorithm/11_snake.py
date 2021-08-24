# 뱀
# acmicpc 3190 (baekjoon)
# LEE SEUNG JAE
# 2021.06.11
#################################

import sys
input = sys.stdin.readline


def move_forward(snake, direction):
    mv = [(0,1), (-1,0), (0,-1), (1,0)] # r,u,l,d

    head = snake[-1]
    next_pos = [x+y for x,y in zip(head, mv[direction])]
    if 0 < next_pos[0] <= N and 0 < next_pos[1] <= N and board[next_pos[0]][next_pos[1]] != 2:
        snake.append(next_pos)
        if board[next_pos[0]][next_pos[1]] == 1:
            board[next_pos[0]][next_pos[1]] = 2
            return snake, True
        else:
            board[next_pos[0]][next_pos[1]] = 2
            tail = snake.pop(0)
            board[tail[0]][tail[1]] = 0
            
            return snake, True
    else:
        return snake, False


N = int(input())
K = int(input())

board = [ [0] *(N+1) for _ in range(N+1) ]
for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1

L = int(input())
rot = []
for _ in range(L):
    a, b = input().split()
    a = int(a)
    rot.append((a,b))

time = 0
snake = [(1,1)]
board[1][1] = 2 # snake
direction = 0   # r,u,l,d = 0,1,2,3
while True:
    snake, end = move_forward(snake, direction)
#    for i in range(N+1):
#        print(board[i])
#    print()

    if end == False:
        time += 1
        print(time)
        break
    else:
        time += 1
    
    if len(rot) > 0 and time == rot[0][0]:
        direc = rot[0][1]
        if direc == "D":
            direction = (direction - 1)
            if direction == -1:
                direction = 3
        elif direc == "L":
            direction = (direction + 1)%4
        rot.remove(rot[0])

