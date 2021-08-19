from collections import deque

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def solution(maps):
    answer = 0
    
    que = deque()
    que.append(((0,0),1))
    visit = set()
    
    while que:
        curr, time = que.popleft()
        
        if curr == (len(maps)-1,len(maps[0])-1):
            answer = max(answer, time)
        
        for i in range(4):
            ny = curr[0] + dy[i]
            nx = curr[1] + dx[i]
            
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if (ny,nx) not in visit and maps[ny][nx] == 1:
                    visit.add((ny,nx))
                    que.append(((ny,nx),time+1))
        
    if answer == 0:
        return -1
    return answer
