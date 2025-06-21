def solution(board, moves):
    answer=0
    stack=[]

    for move in moves:
        col=move-1

        for row in range(len(board)):
            if board[row][col] != 0:
                doll=board[row][col]
                board[row][col]=0  

                if stack and stack[-1] == doll:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(doll)
                break  
    return answer
