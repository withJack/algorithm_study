# 실패율
# 2019 KAKAO BLIND RECRUITMENT
# 2021.05.22. 
# LEE SEUNG JAE
#################################

def solution(N, stages):
    answer = []
    
    fail = dict()
    visitied = dict()
    cnt = stages.count(N+1)
    for i in range(N, 0, -1):
        cnt += stages.count(i)
        if cnt == 0:
            fail[i] = 0
        else:
            fail[i] = stages.count(i) / cnt

    answer = [x[0] for x in sorted(fail.items(), key=lambda x: (-x[1],x[0]))]

    return answer


N, stages = 5, [2,1,2,6,2,4,3,3]
N, stages = 4, [4,4,4,4,4]
print(solution(N, stages))

