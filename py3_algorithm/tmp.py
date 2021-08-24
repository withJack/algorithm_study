dy = [0,1,1]
dx = [1,0,1]

def next_board(m,n, board, empty):
    for i in range(m):
        for j in range(n):
            if empty[i][j]:
                if i == 0:
                    board[i][j] = 0
                if i-1 >= 0:
                    for k in range(i, 0, -1):
                        tmp = board[k-1][j]
                        board[k-1][j] = 0
                        board[k][j] = tmp
    return board


def solution(m, n, board):
    answer = 0
    new_board = [[0]*n for _ in range(m)]
    for i in range(m):
        new_board[i] = list(board[i])
    board = new_board
    
    while True:
        empty = [ [False] * n for _ in range(m) ]
        flag = False
        
        for i in range(m-1):
            for j in range(n-1):
                c = board[i][j]
                if c == 0:
                    continue
                check = True
                for k in range(3):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if board[ny][nx] != c:
                        check = False
                        break
                
                if check:
                    flag = True
                    empty[i][j] = True
                    for k in range(3):
                        ny = i + dy[k]
                        nx = j + dx[k]
                        empty[ny][nx] = True
                
        if flag:
            board = next_board(m,n,board, empty)
        else:
            break
            
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    
    return answer

#print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))
