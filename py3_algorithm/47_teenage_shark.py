# 청소년 상어
# Samsung 공채 (baekjoon 19236)
# Lee Seung Jae
# 2021.07.13
###########################


import sys, copy
input = sys.stdin.readline
from collections import deque


dy = [100,-1,-1,0,1,1,1,0,-1]
dx = [100,0,-1,-1,-1,0,1,1,1]


def next_move(array, now_y, now_x):
    answer = []
    direction = array[now_y][now_x][1]
    ny = now_y + dy[direction]
    nx = now_x + dx[direction]
    while 0 <= ny < 4 and 0 <= nx < 4:
        if 0 < array[ny][nx][0] <= 16:
            answer.append((ny,nx))
        ny += dy[direction]
        nx += dx[direction]

    return answer


def find_fish(array, num):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == num:
                return (i,j)
    return False


def move_fish(array, now_y, now_x):
    for i in range(1, 17):
        fish = find_fish(array, i)
        if fish == False:
            continue
        
        curr_dir = array[fish[0]][fish[1]][1]
        for _ in range(8):
            ny = fish[0] + dy[curr_dir]
            nx = fish[1] + dx[curr_dir]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if not (nx == now_x and ny == now_y):
                    tmp = array[ny][nx]
                    array[ny][nx] = [array[fish[0]][fish[1]][0], curr_dir]
                    array[fish[0]][fish[1]] = tmp
                    break
            curr_dir = curr_dir + 1
            if curr_dir == 9:
                curr_dir = 1


def dfs(array, now_y, now_x, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_y][now_x][0]
    array[now_y][now_x][0] = 0

    move_fish(array, now_y, now_x)

    nxt = next_move(array, now_y, now_x)
    if len(nxt) == 0:
        result = max(result, total)
        return

    for ny, nx in nxt:
        dfs(array, ny, nx, total)


array = [ [None]*4 for _ in range(4) ]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [tmp[2*j], tmp[2*j+1]]

result = 0
dfs(array,0,0,0)
print(result)
