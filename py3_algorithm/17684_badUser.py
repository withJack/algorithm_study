from itertools import permutations

def compare(c, b):
    n = len(c)
    for i in range(n):
        if b[i] == "*":
            continue
        elif b[i] == c[i]:
            continue
        else:
            return False
    return True


def solution(user_id, banned_id):
    answer = set()
    candidate = permutations(user_id, len(banned_id))
    
    for cand in candidate:
        nb = list(banned_id)
        tmp = 0
        for ci in cand:
            n = len(ci)
            check = False
            for bi in nb:
                if n != len(bi):
                    continue
                if compare(ci, bi):
                    nb.remove(bi)
                    check = True
                    break
            if check:
                tmp += 1
        if tmp == len(banned_id):
            answer.add(tuple(sorted(cand)))
    return len(answer)

