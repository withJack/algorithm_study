def solution(s):
    answer = []
    s = list(s)
    
    cnt = 0
    zeros = 0
    while True:
        cnt += 1
        tmp =[]
        for ss in s:
            if ss == "0":
                zeros += 1
            else:
                tmp.append(ss)
        c = len(tmp)
        s = list(str(bin(c))[2:])
        if len(s) == 1:
            break
        
    return [cnt,zeros]
