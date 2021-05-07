# 무지의 먹방라이브
# 2019 KAKAO BLIND RECRUITMENT
# 2021.04.20. 
# LEE SEUNG JAE
#################################

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    h = []
    for idx, food in enumerate(food_times):
        heapq.heappush(h, [food, idx])

    curr_time = 0
    next_ = heapq.heappop(h)
    now = 0
    while k >= curr_time + (len(h)+1)*(next_[0]-now):
        curr_time += (len(h)+1)*(next_[0]-now)
        #h = [[x-next_[0], idx] for x, idx in h]
        now = next_[0]
        next_ = heapq.heappop(h)
        

    heapq.heappush(h,next_)
    h = sorted(h, key = lambda x: x[1])
    res_time = (k-curr_time) % len(h)

    return h[res_time][1] + 1



#food_times = [3,1,2]
#food_times = [4,1,1,5] #4-1, 5-4,6-1.7-4
#food_times = [3,1,1,1,2,4,3] #12 - 6
food_times = [4,3,5,6,2] #7 - 3
k = 7
print(solution(food_times, k))

