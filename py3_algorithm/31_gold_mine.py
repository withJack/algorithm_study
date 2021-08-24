# 금광
# Flipkart 인터뷰
# Lee Seung Jae
# 2021.07.09
###########################

import sys
from collections import deque 
input = sys.stdin.readline

def next_move(a, n, m):
    ans = []
    if a >= m and a%m != 3:
        ans.append(a-m+1)
    if a%m != 3:
        ans.append(a+1)
    if a < (n-1)*m and a%m != 3:
        ans.append(a+m+1)
    return ans


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    high = []
    for start in [i*m for i in range(n)]:
        que = deque([(start, golds[start])])
        highest = 0
        while que:
            curr_place, curr_gold = que.popleft()
            if curr_gold > highest:
                highest = curr_gold
            for nxt in next_move(curr_place, n, m):
                que.append((nxt, curr_gold+golds[nxt]))
        high.append(highest)
    print(max(high))
