# 화성탐사
# ACM-ICPC 기출
# LEE SEUNG JAE
# 2021.05.08
#################################

import sys
sys.stdin = open("input.txt")

import heapq

def can_move(cur, matrix):
    cand = []
    deltas = [(-1,0), (1,0), (0, 1), (0,-1)]
    for dy, dx in deltas:
        nxt = (cur[0] + dy, cur[1] + dx)
        if matrix[nxt[0]][nxt[1]] != -1:
            cand.append(nxt)

    return cand

def dijkstra(matrix, start):
    distances = dict()
    for i in range(len(matrix)-2):
        for j in range(len(matrix)-2):
            distances[(i+1,j+1)] = int('100')
    distances[start] = matrix[start[0]][start[1]]
    que = [(distances[start], start)]

    while que:
        curr_dist, curr_dest = heapq.heappop(que)

        if distances[curr_dest] < curr_dist:
            continue

        for next_dest in can_move(curr_dest, matrix):
            next_dist = curr_dist + matrix[next_dest[0]][next_dest[1]]
            if next_dist < distances[next_dest]:
                distances[next_dest] = next_dist
                heapq.heappush(que, [next_dist, next_dest])
    return distances


# test num
T = int(input())
for _ in range(T):
    # each test matrix
    N = int(input())
    matrix = []
    matrix.append([-1 for _ in range(N+2)])
    for _ in range(N):
        matrix.append([-1]+list(map(int, input().split(" ")))+[-1])
    matrix.append([-1 for _ in range(N+2)])
    # Dijkstra algorithm
    start = (1,1)
    end = (N,N)
    answer = dijkstra(matrix, start)
    print(answer[end])
