# 최종 순위
# NWERC 2010 (baekjoon 3665)
# Lee Seung Jae
# 2021.06.29
###########################

import sys
from collections import deque
input = sys.stdin.readline


def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        if len(q) > 1: 
            return -2
        curr = q.popleft()
        result.append(curr)

        for i in range(1, n+1):
            if edge[curr][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)


    if len(result) != n:
        return -1
    else:
        return result


N = int(input())

for _ in range(N):
    n = int(input())
    last_rank = list(map(int, input().split()))
    indegree = [0] * (n+1)
    edge = [ [False]*(n+1) for _ in range(n+1) ]
    
    for i in range(n):
        for j in range(i+1, n):
            edge[last_rank[i]][last_rank[j]] =True
            indegree[last_rank[j]] += 1
        
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if edge[a][b]:
            edge[a][b] = False
            edge[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            edge[b][a] = False
            edge[a][b] = True
            indegree[b] += 1
            indegree[a] -= 1
            

    answer = topology_sort()
    if answer == -1:
        print("IMPOSSIBLE")
    elif answer == -2:
        print("?")
    else:
        for a in answer:
            print(a, end=' ')
        print()
    

