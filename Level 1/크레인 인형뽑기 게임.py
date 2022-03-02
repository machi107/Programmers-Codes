def solution(board, moves):
    zz=[]
    answer=0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] !=0:
                if len(zz) and zz[len(zz)-1] ==board[j][moves[i]-1]:
                    zz=zz[:-1]
                    answer+=2
                else:
                    zz.append(board[j][moves[i]-1])
                board[j][moves[i]-1]=0
                break
    

    return answer
