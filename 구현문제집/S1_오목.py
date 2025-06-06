board=[list(map(int,input().split())) for _ in range(19)]

def check_five(x,y,dx,dy,color):
    for i in range(5):
        if board[x+i*dx][y+i*dy]!=color:
            return False
    #육목 방지
    nx=x-dx
    ny=y-dy
    if 0<=nx<19 and 0<=ny<19:
        if board[nx][ny]==color:
            return False
    nx=x+5*dx
    ny=y+5*dy
    if 0<=nx<19 and 0<=ny<19:
        if board[nx][ny]==color:
            return False
    return True

def 오목(board):
    for i in range(19):
        for j in range(19):
            if board[i][j]==0:
                continue
            color=board[i][j]
            # 방향: (dx, dy)
            for dx, dy in [(0,1), (1,0), (1,1), (-1,1)]:
                nx=i+4*dx
                ny=j+4*dy
                if 0<=nx<19 and 0<=ny<19:
                    if check_five(i,j,dx,dy,color):
                        print(color)
                        print(i+1,j+1)
                        return
    print(0)

오목(board)
