def solution(s):
    answer = 0
    
    flag = (False,0)
    skip = 0
    tmp = []
    for c in s:
        if skip != 0:
            skip -= 1
            continue
            
        if flag[0]:
            if flag[1] == 't':
                if c == 'h':
                    skip = 3
                    tmp.append('3')
                elif c == 'w':
                    skip = 1
                    tmp.append('2')
            elif flag[1] == 'f':
                if c == 'o':
                    skip = 2
                    tmp.append('4')
                elif c == 'i':
                    skip = 2
                    tmp.append('5')
            elif flag[1] == 's':
                if c == 'i':
                    skip = 1
                    tmp.append('6')
                elif c == 'e':
                    skip = 3
                    tmp.append('7')
            flag = (False,0)
            continue
                
        if 'a' <= c <= 'z':
            if c == 'z':
                skip = 3
                tmp.append('0')
            elif c == 'o':
                skip = 2
                tmp.append('1')
            elif c == 't':
                flag = (True, c)
            elif c == 'f':
                flag = (True, c)
            elif c == 's':
                flag = (True, c)
            elif c == 'e':
                skip = 4
                tmp.append('8')
            elif c == 'n':
                skip = 3
                tmp.append('9')
        
        else:
            tmp.append(str(c))
    
            
    return int("".join(tmp))
