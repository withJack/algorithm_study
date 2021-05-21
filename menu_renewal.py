# 메뉴 리뉴얼
# 2021 KAKAO BLIND RECRUITMENT
# 2021.05.18. 
# LEE SEUNG JAE
#################################

from itertools import combinations

def solution(orders, course):
    answer = []
    tmp = dict()
    for order in orders:
        for i in course:
            for a in list(combinations(order,i)):
                a = tuple(sorted(a))
                if a in tmp.keys():
                    tmp[a] += 1
                else:
                    tmp[a] = 1

    max_tmp = {x:0 for x in course}
    for a, b in tmp.items():
        if b >= 2:
            if max_tmp[len(a)] <= b:
                max_tmp[len(a)] = b
    for a, b in tmp.items():
        if b == max_tmp[len(a)]:
            answer.append("".join(a))
    
    answer.sort()
    print(answer)
    
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
solution(orders, course)

