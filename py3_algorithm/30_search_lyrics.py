# 가사 검색
# 2020 KAKAO BLIND RECRUITMENT
# Lee Seung Jae
# 2021.07.09
###########################

import sys
from itertools import permutations 
input = sys.stdin.readline


def solution(words, queries):
    answer = []
    
    for query in queries:
        cnt = 0
        q_len = len(query)
        
        for word in words:
            q_cnt = 1
            # ? in prefix
            if query[0] == '?':
                for i in range(1, q_len):
                    if query[i] != '?':
                        break
                    q_cnt += 1

                if word[q_cnt:] == query[q_cnt:]:
                    cnt += 1

            # ? in suffix
            else:
                for i in range(q_len-2, 0, -1):
                    if query[i] != '?':
                        break
                    q_cnt += 1
                
                if word[:-q_cnt] == query[:-q_cnt]:
                    cnt += 1
        answer.append(cnt)
    return answer


from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: 
        array[len(word)].append(word) 
        reversed_array[len(word)].append(word[::-1]) 

    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: 
        if q[0] != '?': 
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: 
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer
