# 어두운 길
# University of Ulm Local Contest
# Lee Seung Jae
# 2021.06.11
###################################

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


N, M = map(int, input().split())

costs = []
for _ in range(M):
    a, b, c = map(int, input().split())
    costs.append((c,a,b))
costs.sort()

parents = [ i for i in range(N) ]

total = 0
results = 0
for cost in costs:
    c, a, b = cost
    total += c
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        results += c

print(total - results)
