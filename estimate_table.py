# 예상 대진표
# 2017 팁스타운
# 2021.05.18. 
# LEE SEUNG JAE
#################################

def solution(n,a,b):
    answer = 0
    
    while True:
        answer += 1
        if a % 2:
            a = (a+1)//2
        else:
            a = a//2
        if b % 2:
            b = (b+1)//2
        else:
            b = b//2
        print(a,b)
        if a == b: break

    return answer

N, A, B = map(int, input().split())
solution(N,A,B)

