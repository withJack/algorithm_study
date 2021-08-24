# 탑승구
# baekjoon 10775
# 2021.06.07
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



G = int(input())
P = int(input())

docked = [0] * (G+1)
for i in range(G):
    docked[i+1] = i+1

cnt = 0
for _ in range(P):
    data = find_parent(docked, int(input()))
    if data == 0:
        break
    union_parent(docked, data, data-1)
    cnt += 1

print(cnt)
