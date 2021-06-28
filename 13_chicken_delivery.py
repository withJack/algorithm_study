# 치킨 배달
# Samsung SW test (baekjoon 15686)
# Lee Seung Jae
# 2021.06.28
###########################

import sys
from itertools import combinations
input = sys.stdin.readline

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def town_chicken(house,chicken):
    cnt = 0
    for h in house:
        minimum = 101
        for c in chicken:
            tmp = dist(h,c)
            if tmp < minimum:
                minimum = tmp
        cnt += minimum
    return cnt 

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

mini = 1e+9
for ch in combinations(chicken, M):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if mini <= sumv: break
    if sumv < mini: mini = sumv
print(mini)

#for i in range(M, 0, -1):
#    chick = combinations(chicken, i)
#    for chi in chick:
#        tmp = town_chicken(house, chi)
#        if tmp < mini:
#            mini = tmp
#print(mini)
