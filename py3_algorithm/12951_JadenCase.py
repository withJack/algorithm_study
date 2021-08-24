def solution(s):
    answer = ''
    
    flag = True
    for ss in s:
        if flag:
            if ss == " ":
                answer += ss
                continue
            if 'a' <= ss <= 'z':
                answer += ss.upper()
            else:
                answer += ss
            flag = False
        else:
            if ss == ' ':
                flag = True
                answer += ss
            elif 'A' <= ss <= 'z':
                answer += ss.lower()
            else:
                answer += ss
            
    return answer
