# 정확한 순위
# K 대회 기출문제
# 2021.04.21.
# LEE SEUNG JAE
###############################

import sys

INF = int(501)

sys.stdin = open("input.txt")

N, M = map(int, input().split(" "))
matrix = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    matrix[i][i] = 0

for _ in range(M):
    f,t = map(int, input().split())
    matrix[f-1][t-1] = 1


# Floyd-Warshal algorithm
for mid in range(N):
    for f in range(N):
        for t in range(N):
            matrix[f][t] = min(matrix[f][t], matrix[f][mid] + matrix[mid][t])

for i in range(N):
    print(matrix[i])


answer = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[i][j] != INF or matrix[j][i] != INF:
            cnt += 1
    
    if cnt == N:
        answer += 1

print(answer)

