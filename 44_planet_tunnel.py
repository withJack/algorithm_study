# 행성 터널
# COCI (baekjoon 2887)
# Lee Seung Jae
# 2021.06.25
###########################

import sys
input = sys.stdin.readline


def distance(p1, p2):
    return min(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2]-p2[2]))

def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[a] = b
    else:
        parents[b] = a


N = int(input())

parents = [ i for i in range(N) ]

x = []
y = []
z = []

planets = []
for i in range(N):
    a, b, c = map(int, input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

edges = []  # (cost, a, b)
for i in range(N-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result += cost
print(result)
    
