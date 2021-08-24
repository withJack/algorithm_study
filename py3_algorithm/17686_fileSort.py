def solution(files):
    answer = []
    
    li = []
    cnt = 0
    for file in files:
        newfile = list(file)
        head, number = "", ""
        check = 0
        
        for f in newfile:
            if check == 0 and f.isdigit():
                check = 1
            elif check == 1 and not f.isdigit():
                check = 2
                
            if check == 0:
                head += f.lower()
            elif check == 1:
                number += f
        li.append([[head, int(number), cnt], file])
        cnt += 1
    
    li.sort(key=lambda x:(x[0][0], x[0][1], x[0][2]))
    
    for l in li:
        answer.append(l[1])
                
    return answer
