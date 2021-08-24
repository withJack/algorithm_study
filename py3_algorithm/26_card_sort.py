# 카드 정렬하기
# acmicpc 1715 (baekjoon)
# LEE SEUNG JAE
# 2021.06.02
#################################
import sys
import heapq

N = int(sys.stdin.readline())
cards = []
for _ in range(N):
    cards.append(int(sys.stdin.readline()))

answer = 0
heapq.heapify(cards)
while len(cards) > 1:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    heapq.heappush(cards, c1+c2)
    answer += c1+c2

print(answer)
