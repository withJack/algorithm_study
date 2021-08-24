#def solution(board):
#    answer = [0]
#    if len(board) == 1 and len(board[0]) == 1:
#        if board[0][0] == 0:
#            return 0
#        elif board[0][0] == 1:
#            return 1
#        
#    for i in range(len(board)):
#        for j in range(len(board[0])):
#            if board[i][j] != 1:
#                continue
#            l = min(len(board)-i, len(board[0])-j)
#            
#            for d in range(l):
#                check = False
#                for ii in range(d+1):
#                    if board[i+ii][j+d] == 0 or board[i+d][j+ii] == 0:
#                        check = True
#                        break
#                if check:
#                    break
#                else:
#                    answer.append(d)
#    if max(answer) == 0:
#        return 0
#    
#    return (max(answer)+1)**2


def solution(board):
    answer = 0
    row = len(board)
    colum=len(board[0])
    for i in range(row):
        for j in range(colum):
            if i==0 or j==0:
                continue
            if board[i][j]!=0:
                board[i][j]=min(board[i-1][j-1],min(board[i-1][j],board[i][j-1]))+1
    li=[]
    for i in range(row):
        li.append(max(board[i]))
    return max(li)**2
