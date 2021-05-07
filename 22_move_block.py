# 블록 이동하기
# 2020 KAKAO BLIND RECRUITMENT
# 2021.05.01. 
# LEE SEUNG JAE
#################################

from collections import deque

def can_move(cur1, cur2, new_board):
    cand = []
    # move up/down/right/left
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in DELTAS:
        nxt1 = (cur1[0] + dy, cur1[1] + dx)
        nxt2 = (cur2[0] + dy, cur2[1] + dx)
        if new_board[nxt1[0]][nxt1[1]] == 0 and new_board[nxt2[0]][nxt2[1]] == 0:
            cand.append((nxt1, nxt2))

    # rotation
    if cur1[0] == cur2[0]: # lying down
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[0]+d][cur1[1]] == 0 and new_board[cur2[0]+d][cur2[1]] == 0:
                cand.append((cur1, (cur1[0]+d, cur1[1])))
                cand.append((cur2, (cur2[0]+d, cur2[1])))
    elif cur1[1] == cur2[1]: # stand up
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[0]][cur1[1]+d] == 0 and new_board[cur2[0]][cur2[1]+d] == 0:
                cand.append(((cur1[0], cur1[1]+d), cur1))
                cand.append(((cur2[0], cur2[1]+d), cur2))
    else:
        print("error")

    return cand

def solution(board):
    # set board border 
    N = len(board)
    new_board = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    # robot insert with distance, visit set
    que = deque([((1, 1), (1, 2), 0)])
    visit = set([((1, 1), (1, 2))])

    while que:
        cur1, cur2, count = que.popleft()
        # end condition
        if cur1 == (N, N) or cur2 == (N, N):
            return count

        # next moves: list of sets
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in visit:
                que.append((*nxt, count+1))
                visit.add(nxt)





#print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
