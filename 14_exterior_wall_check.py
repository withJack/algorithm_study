# 외벽 점검
# 2020 KAKAO BLIND RECRUITMENT
# Lee Seung Jae
# 2021.07.09
###########################

import sys
from itertools import permutations 
input = sys.stdin.readline

def solution(n, weak, dist):
    answer = len(dist) + 1

    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i]+n)

    for i in range(weak_len):
        start = [weak[j] for j in range(i, i+weak_len)]
        friends = permutations(dist, len(dist))
        
        for friend in friends:
            idx = 0
            count = 1
            possible = start[0] + friend[idx]
            for j in range(weak_len):
                if start[j] > possible:
                    count += 1
                    if count > len(friend):
                        break
                    idx += 1
                    possible = friend[idx] + start[j]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1,5,6,10], [1,2,3,4]))
