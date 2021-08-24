# 기둥과 보 설치
# 2020 KAKAO BLIND RECRUITMENT
# LEE SEUNG JAE
# 2021.06.25
#################################

def isPossible(current):
    for x, y, what in current:
        # pillar
        if what == 0:
            if y == 0 or (x-1,y,1) in current or (x,y,1) in current or (x,y-1,0) in current:
                continue
            return False
            
        # blanket
        elif what == 1:
            if (x,y-1,0) in current or (x+1,y-1,0) in current or ((x-1,y,1) in current and (x+1,y,1) in current):
                continue                                                                
            return False
    return True


def solution(n, build_frame):
    answer = []
               
    for build in build_frame:
    # add
        if build[3] == 1:
            answer.append((build[0],build[1],build[2]))
            if isPossible(answer) == False: 
                answer.remove((build[0],build[1],build[2]))
            
        # remove
        elif build[3] == 0:
            answer.remove((build[0],build[1],build[2]))
            if isPossible(answer) == False:
                answer.append((build[0],build[1],build[2]))

       
    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
