# 숨바꼭질
# USACO
# 2021.05.15. 
# LEE SEUNG JAE
#################################

import sys
sys.stdin = open("40_input.txt")

import heapq

def dijkstra(barn):
    distances = [0] + [10**9] * (len(barn)-1)
    que = [(0,0)]

    while que:
        curr_dist, curr_dest = heapq.heappop(que)
        
        if distances[curr_dest] < curr_dist:
            continue
        
        for new_dest in barn[curr_dest]:
            if 1 + curr_dist < distances[new_dest]:
                distances[new_dest] = 1 + curr_dist
                heapq.heappush(que, [distances[new_dest], new_dest])

    return distances

N, M = map(int, input().split())

barn = dict()
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a in barn.keys():
        barn[a].append(b)
    else:
        barn[a] = [b]

    if b in barn.keys():
        barn[b].append(a)
    else:
        barn[b] = [a]
    

sb = dijkstra(barn)
max_room = max(sb)
cnt = 0
loc = []
for i, room in enumerate(sb):
    if max_room == room:
        loc.append(i)
        cnt += 1
#print(sb.index(max_room)+1,max_room,sb.count(max_room))
print(loc[0]+1,max_room,cnt)
