# 자물쇠와 열쇠
# 2020 KAKAO BLIND RECRUITMENT
# 2021.06.02
# LEE SEUNG JAE
#################################



def get_rotate(key):
    M = len(key)
    tmp = [[0] * M for _ in range(M)] 
    for r in range(M):
        for c in range(M):
            tmp[c][M-1-r] = key[r][c]
    
    return tmp


def solution(key, lock):

    M = len(key)
    N = len(lock)
    cnt = 0
    new_lock = [[1] *(N+2*M-2) for _ in range(N+2*M-2)]
    for i, l in enumerate(lock):
        for j, ll in enumerate(l):
            if ll == 0:
                cnt += 1
                new_lock[i+M-1][j+M-1] = 0

    for i in range(N+M-1):
        for j in range(N+M-1):
            # rotate
            rotate_key = key
            for _ in range(4):
                out = 0
                rotate_key = get_rotate(rotate_key)
                tmp = 0
                for ii in range(M):
                    for jj in range(M):
                        if M-1 <= i+ii < N+M-1 and M-1 < j+jj <= N+M-1:
                            if rotate_key[ii][jj] + new_lock[i+ii][j+jj] != 1:
                                out = 1
                                answer = False
                                break
                            elif rotate_key[ii][jj] == 1:
                                tmp += 1
                    if out == 1:
                        break
                if tmp == cnt:
                    return True
                            
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

