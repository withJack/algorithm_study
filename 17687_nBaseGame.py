def solution(n, t, m, p):
    answer = ''
    length = m * t
    candidate = '0'
    num = 0
    alpha = '0123456789ABCDEF'
    
    while len(candidate) < length: 
        res = ''
        number = num
        while True:  
            if number == 0: 
                break
            res += alpha[number%n]
            number //= n
        
        num += 1
        candidate += res[::-1] # reverse
    
    turns = [p+m*i-1 for i in range(t)]
    for i in turns:
        answer += candidate[i]
        
    return answer
