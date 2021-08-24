# 아기 상어
# Samsung 공채 (baekjoon 16236)
# Lee Seung Jae
# 2021.07.09
###########################

moves = [[0,1],[0,-1],[-1,0],[1,0]]

import sys, heapq
input = sys.stdin.readline
from collections import deque


def next_move(dy,dx, N):
    
    answer = []
    # u l r d
    if dy-1 >= 0:
        answer.append((dy-1, dx))
    if dx -1 >= 0:
        answer.append((dy, dx-1))
    if dx + 1 < N:
        answer.append((dy, dx+1))
    if dy+1 < N:
        answer.append((dy+1,dx))

    return answer


def bfs(graph, baby):
    que = deque([(baby[0], baby[1], 0)])
    visit = set([(baby[0], baby[1])])
    heap = []

    while que:
        curr_x, curr_y, curr_time = que.popleft()

        for nxt in next_move(curr_x, curr_y, N):
            if (nxt[0],nxt[1]) not in visit: #and graph[nxt[0]][nxt[1]] <= size:
                visit.add((nxt[0],nxt[1]))
                if 0 == graph[nxt[0]][nxt[1]] or graph[nxt[0]][nxt[1]] == size:
                    que.append((nxt[0],nxt[1],curr_time+1))
                elif 0 < graph[nxt[0]][nxt[1]] < size:
                    heapq.heappush(heap, (curr_time+1, nxt[0], nxt[1]))

    if heap:
        return heap[0]
    else:
        return -1
                    

N = int(input())

graph = [[]*N for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

fishes = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            baby = (i,j)
            graph[i][j] = 0
        elif 1 <= graph[i][j] <= 6:
            fishes.append((i, j))


size = 2
eat = 0
time = 0

while fishes:
    if eat == size:
        eat = 0
        size += 1
    
    steps = bfs(graph, baby)
    if steps == -1:
        break
    else:
        cnt, ny, nx = steps
        time += cnt
        eat += 1
        fishes.remove((ny,nx))
        graph[ny][nx] = 0
        baby = (ny,nx)

print(time)


exit()

closest = 100
for fish in fishes: 
    if fish[0] > baby[0]:
        continue
    dist = abs(fish[1]-baby[1]) + abs(fish[2]-baby[2])
    if dist < closest:
        closest = dist
        close_fish = fish
print(close_fish)
que = deque([(start, 2)])   #place, size

