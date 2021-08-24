# 고정점 찾기
# Amazon Interview
# Lee Seung Jae
# 2021.06.25
########################

import sys
input = sys.stdin.readline

def BS(array, start, end):
    while start <= end:
        mid = (start+end) // 2
        if mid == array[mid]: 
            return mid
        elif mid < array[mid]:
            end = mid - 1
        elif mid > array[mid]:
            start = mid + 1

    return -1


N = int(input())
points = list(map(int, input().split()))

print(BS(points, 0, N))

