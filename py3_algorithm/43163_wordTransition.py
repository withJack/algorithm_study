from collections import deque

def next_move(curr, words):
    c = list(curr)
    n = len(curr)
    nxt = []
    for word in words:
        cnt = 0
        nw = list(word)
        for i in range(n):
            if nw[i] == c[i]:
                continue
            else:
                cnt += 1
            if cnt > 1:
                break
        if cnt <= 1:
            nxt.append(word)
            
    return nxt

def solution(begin, target, words):
    answer = 0
    
    que = deque()
    que.append([begin, 0])
    visit = set()
    
    while que:
        curr, time = que.popleft()
        
        if curr == target:
            return time
        
        for nxt in next_move(curr, words):
            if nxt not in visit:
                visit.add(nxt)
                que.append([nxt, time+1])
    
    return answer
