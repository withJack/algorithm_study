# 전쟁-전투
# baekjoon 1303
# 2021.06.08
# LEE SEUNG JAE
#################################

import sys
input = sys.stdin.readline

from collections import deque

def next_move(curr_pos):
    moves = [[0,1], [1,0], [0,-1], [-1,0]]
    next_moves = []
    a = curr_pos[0]
    b = curr_pos[1]
    for move in moves:
        if 0 <= a + move[0] < N and 0 <= b + move[1] < M:
            if visited[a+move[0]][b+move[1]] == 0:
                next_moves.append((a+move[0], b+move[1]))
    return next_moves


N, M = map(int, input().split())

board = [ [] for _ in range(M) ] 
visited = [ [0] * N for _ in range(M) ]

for i in range(N):
    board[i] = list(input().strip()) 


cnt = {'W':0, 'B':0}
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            visited[i][j] = 1
            q = deque()

            q.append(((i,j),board[i][j]))
            tmp = 1
            while q:
                curr_pos, team = q.popleft()
                
                for new_pos in next_move(curr_pos):
                    if board[new_pos[0]][new_pos[1]] == team:
                        visited[new_pos[0]][new_pos[1]] = 1
                        q.append([(new_pos[0], new_pos[1]),team])
                        tmp += 1
            cnt[board[i][j]] += tmp*tmp

print( cnt)
