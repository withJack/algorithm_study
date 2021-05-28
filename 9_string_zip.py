# 문자열 압축
# 2020 KAKAO BLIND RECRUITMENT
# 2021.05.22. 
# LEE SEUNG JAE
#################################

def solution(s):
    answer = 1001 
    length = len(s)
    if length == 1:
        return 1

    for i in range(1, int(length/2)+1):
        result = []
        tmp = []
        for j in range(0, length-i+1, i):
            tmp.append(s[j:j+i])
        tmp.append(s[j+i:])
        
        cnt = 1
        prev = ""
        for sub in tmp:
            curr = sub
            if curr == prev:
                cnt +=1
            elif prev != "":
                if cnt > 1:
                    result.append(str(cnt))
                result.append(prev)
                cnt = 1
            prev = curr
        if cnt > 1:
            result.append(str(cnt))
        result.append(prev)

        result_len = 0
        for re in result:
            result_len += len(re)

        if result_len < answer:
            answer = result_len

    return answer


print(solution(input()))

