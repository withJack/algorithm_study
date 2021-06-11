# 바이러스 
# baekjoon 2606
# 2021.06.08
# LEE SEUNG JAE
#################################

import sys
input = sys.stdin.readline


def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N = int(input())
P = int(input())

parents = [ i for i in range(N+1) ]
for _ in range(P):
    a, b = map(int,input().split())
    pa = find_parent(parents, a)
    pb = find_parent(parents, b)
    
    if pa != pb:
        union_parent(parents, a, b)

ans = find_parent(parents, 1)
cnt = 0
for p in range(1, N+1):
    tmp = find_parent(parents, p)
    if tmp == ans:
        cnt += 1

print(cnt-1)
