from collections import deque

def solution(priorities, location):
    answer = 0
    n = len(priorities)
    graph = []
    prior = dict()
    for i, p in enumerate(priorities):
        graph.append([i,p])
        prior[i] = p
    que = deque(graph)
    flag = False
    while que:
        cur_pos, cur_prior = que.popleft()

        for i in prior.keys():
            if cur_prior < prior[i]:
                que.append([cur_pos,cur_prior])
                flag = True
                break

        if flag:
            flag = False
            continue
        else:
            answer += 1
            prior.pop(cur_pos, None)
            if cur_pos == location:
                return answer
    return answer
