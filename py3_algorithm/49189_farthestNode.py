from collections import deque

def bfs(graph, start):
    que = deque([(start, 0)])
    visit = set([start])
    time = [ 10e9 for _ in range(len(graph)+1)]
    
    while que:
        curr_pos, curr_time = que.popleft()
        
        if curr_time < time[curr_pos]:
            time[curr_pos] = curr_time
        
        for nxt in graph[curr_pos]:
            if nxt not in visit:
                visit.add(nxt)
                que.append((nxt,curr_time+1))
                
    return time

def solution(n, edge):
    answer = 0
    graph = { i:[] for i in range(1, n+1) }
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    time = bfs(graph,1)
    
    tmp = 0
    for t in time[1:]:
        if t > tmp:
            tmp = t
            answer = 1
        elif t == tmp:
            answer += 1
    
    return answer
