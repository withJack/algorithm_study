def solution(name):
    answer = 0
    
    # 1..n
    name = list(name)
    n = len(name)
    
    pos = 0
    while True:
        answer += min(ord(name[pos])-ord('A'), ord('Z')-ord(name[pos])+1)
        name[pos] = 'A'
                
        # terminal condition
        if name.count('A') == n:
            return answer
        
        # greedy
        l, r = 1, 1
        for i in range(1,n):
            if name[pos-i] == 'A':
                l += 1
            else: 
                break
        
        for i in range(1,n):
            if name[pos+i] == 'A':
                r += 1
            else: 
                break

        if l < r:
            answer += l
            pos -= l
        else:
            answer += r
            pos += r
    
    return answer
