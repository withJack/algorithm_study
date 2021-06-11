# 정렬된 배열에서 특정 수의 개수 구하기
# Zoho 인터뷰
# LEE SEUNG JAE
# 2021.06.11
#################################
import sys
import heapq

def binary_search_first(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if mid == 0 or array[mid-1] < target and array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def binary_search_last(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if mid == len(array) - 1 or array[mid+1] > target and array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


N, x = map(int, input().split())
sorted_li = list(map(int, input().split()))

first = binary_search_first(sorted_li, x, 0, N-1)
if first == -1:
    print(-1)
else:
    last = binary_search_last(sorted_li, x, 0, N-1)
    print(last-first+1)
