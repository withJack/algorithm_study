from collections import deque

def solution(s):
    
    stack = deque([])
    tmp = ""
    while True:      
        for ss in s:
            if ss == tmp:
                stack.pop()
                if stack:
                    tmp = stack.pop()
                    stack.append(tmp)
                else:
                    tmp = ""
            else:
                stack.append(ss)
                tmp = ss
                
        if stack:
            return 0
        else:
            return 1
        
    return -1
