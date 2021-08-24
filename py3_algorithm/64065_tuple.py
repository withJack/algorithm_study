def solution(s):
    answer = []
    new_s = s[1:len(s)-1]
    
    cnt = 0
    tmp_dict = dict()
    flag = False
    tmp = ''
    for i in range(len(new_s)):
        if s[i] == "{":
            tmp_dict[cnt] = set()
            flag = True
            continue
        elif s[i] == "}":
            tmp_dict[cnt].add(int(tmp))
            tmp = ''
            cnt += 1
            flag = False
            continue
        if flag:
            if s[i] == ',':
                tmp_dict[cnt].add(int(tmp))
                tmp = ''
            else:
                tmp += s[i]
    tmp_dict[cnt].add(int(tmp))
    for i in sorted(tmp_dict, key=lambda k: len(tmp_dict[k])):
        for tmp in tmp_dict[i]:
            if tmp not in answer:
                answer.append(tmp)
    return answer
