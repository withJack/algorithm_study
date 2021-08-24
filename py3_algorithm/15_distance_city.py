# 특정거리의 도시 찾
# (baekjoon 18352)
# Lee Seung Jae
# 2021.07.09
###########################

import sys
input = sys.stdin.readline
from collections import deque

def find_city(graph, start, dist):
    que = deque([(start, 0)])
    visit = [start]
    answer = []
    while que:
        curr_place, curr_dist = que.popleft()
        if curr_dist == dist:
            answer.append(curr_place)
            continue

        for nxt in graph[curr_place]:
            if nxt not in visit:
                que.append((nxt, curr_dist+1))
                visit.append(nxt)

    return answer


N, M, K, X = map(int, input().split())

graph = { i:[] for i in range(N+1) }

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

ans = find_city(graph, X, K)
ans.sort()
if len(ans) == 0:
    print(-1)
else:
    for a in ans:
        print(a)
