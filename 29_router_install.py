# 공유기 설치
# (baekjoon 15686)
# Lee Seung Jae
# 2021.06.28
###########################

import sys
input = sys.stdin.readline


N, C = map(int, input().split())

house = []
for _ in range(N):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]

result = 0
while start <= end:
    mid = (start+end) // 2
    current = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= current+mid:
            current = house[i]
            count += 1

    if count >= C:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)
