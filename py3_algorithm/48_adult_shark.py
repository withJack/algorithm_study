# 어른 상어
# Samsung 공채 (baekjoon 19237)
# Lee Seung Jae
# 2021.07.14
###########################


import sys, copy
input = sys.stdin.readline
from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


N, M, k = map(int, input().split())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

# up down left right : 1 2 3 4
directions = list(map(int, input().split()))

prior = [ [] for _ in range(M) ]
for i in range(M):
    for j in range(4):
        prior[i].append(list(map(int, input().split())))

scent = [ [[0,0]]*N for _ in range(N) ]


def belch():
    for i in range(N):
        for j in range(N):
            if scent[i][j][1] > 0:
                scent[i][j][1] -= 1
            if array[i][j] != 0:
                scent[i][j] = [array[i][j], k]


def move_shark():
    new_array = [ [0] * N for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            if array[i][j] > 0:
                curr_dir = directions[array[i][j]-1]
                found = False
                for a in range(4):
                    ny = i + dy[prior[array[i][j] - 1][curr_dir - 1][a] - 1]
                    nx = j + dx[prior[array[i][j] - 1][curr_dir - 1][a] - 1]
                    if 0 <= ny < N and 0 <= nx < N:
                        if scent[ny][nx][1] == 0:
                            directions[array[i][j] - 1] = prior[array[i][j] - 1][curr_dir - 1][a]
                            if new_array[ny][nx] == 0:
                                new_array[ny][nx] = array[i][j]
                            else:
                                new_array[ny][nx] = min(new_array[ny][nx], array[i][j])
                            found = True
                if found == True:
                    continue

                for b in range(4):
                    ny = i + dy[prior[array[i][j] - 1][curr_dir - 1][a] - 1]
                    nx = j + dx[prior[array[i][j] - 1][curr_dir - 1][a] - 1]
                    if 0 <= ny < N and 0 <= nx < N:
                        if scent[ny][nx][0] == array[i][j]:
                            directions[array[i][j] -1] = prior[array[i][j] - 1][curr_dir - 1][b]
                            new_array[ny][nx] = array[i][j]
                            break
    return new_array


def check_one():
    for i in range(N):
        for j in range(N):
            if array[i][j] > 1:
                return False
    return True


time = 0
while True:
    belch()
    array = move_shark()
    time += 1
    
    if check_one:
        print(time)
        break
    
    if time >= 1000:
        print(-1)
        break
    
