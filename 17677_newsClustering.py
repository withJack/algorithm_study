def solution(str1, str2):
    answer = 0
    
#    str1 = [s.lower() for s in str1 if s.isalpha()]
#    str2 = [s.lower() for s in str2 if s.isalpha()]

    len_1 = len(str1)
    len_2 = len(str2)
    
    dict_1, dict_2 = dict(), dict()
    
    for i in range(len_1-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1, s2 = str1[i].lower(), str1[i+1].lower()
            if (s1,s2) in dict_1.keys():
                dict_1[(s1,s2)] += 1
            else:
                dict_1[(s1,s2)] = 1
    
    for i in range(len_2-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s1, s2 = str2[i].lower(), str2[i+1].lower()
            if (s1,s2) in dict_2.keys():
                dict_2[(s1,s2)] += 1
            else:
                dict_2[(s1,s2)] = 1
    
    if len(dict_1) == 0 and len(dict_2) == 0:
        return 1*65536
    
    set_1 = set(dict_1.keys())
    set_2 = set(dict_2.keys())
    
    # intersect
    upper = 0 
    for s in set_1.intersection(set_2):
        upper += min(dict_1[s], dict_2[s])
    
    # union
    lower = 0
    for s in set_1.union(set_2):
        if s in set_1 and s in set_2:
            lower += max(dict_1[s], dict_2[s])
        elif s not in set_1:
            lower += dict_2[s]
        elif s not in set_2:
            lower += dict_1[s]
    
    return int(upper/lower*65536)
