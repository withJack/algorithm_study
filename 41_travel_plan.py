# 여행 계획
# baekjoon 1976
# 2021.05.28. 
# LEE SEUNG JAE
#################################

import sys
input = sys.stdin.readline


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())

parent = [x for x in range(N+1)]

for i in range(N):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if i < j and t == 1:
            union_parent(parent, i+1, j+1)

travel_plan = list(map(int, input().split()))

possible = "YES"
for i in range(M-1):
    if find_parent(parent, travel_plan[i]) != find_parent(parent, travel_plan[i+1]):
        possible = "NO"
        break

print(possible)
