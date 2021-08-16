from collections import deque

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def find_close(place, p):
    que = deque([p])
    visit = [[-1 for _ in range(5)] for _ in range(5)]
    visit[p[0]][p[1]] = 0
    
    while que:
        cy, cx = que.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if place[ny][nx] != "X" and visit[ny][nx] == -1:
                    visit[ny][nx] = visit[cy][cx] + 1
                    que.append((ny,nx))
#    for i in range(5):
#        print(visit[i])
    return visit


def solution(places):
    answer = []
    
    for place in places:
        people = []
        for i, p in enumerate(place):
            for j, c in enumerate(p):
                if c == "P":
                    people.append((i,j))
        
        if len(people) == 0:
            answer.append(1)
            continue
        
        flag = True
        for p in people:
            visit = find_close(place, p)
            for pp in people:
                if pp is not p:
                    print(pp)
                    if -1 < visit[pp[0]][pp[1]] <= 2:
                        flag = False
                        break
            if not flag: 
                break
        
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
