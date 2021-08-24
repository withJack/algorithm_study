from itertools import combinations
def solution(relation):
    answer = 0
    idxes = [i for i in range(len(relation[0]))]
    ans = []
    for i in range(1, len(relation[0])+1):
        for combi in list(combinations(idxes, i)):
            tmp1 = []
            for rel in relation:
                tmp2 = []
                for c in combi:
                    tmp2.append(rel[c])
                tmp1.append(tmp2)
                
            seen = []
            unique_list = [x for x in tmp1 if x not in seen and not seen.append(x)]
            if len(tmp1) == len(unique_list):
                ans.append(combi)
    
    answer = set(ans[:])
    print(answer, ans)
    for i in range(len(ans)):
        for j in range(i+1,len(ans)):
            if len(ans[i])==len(set(ans[i]).intersection(set(ans[j]))):
                answer.discard(ans[j])
        
    return len(answer)
