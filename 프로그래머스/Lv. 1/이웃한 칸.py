def solution(board, h, w):
    cnt=0
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    size=len(board)
    
    for i in range(4):
        nh=h+dx[i]
        nw=w+dy[i]
        if 0 <=nh<size and 0<=nw<size:
            if board[nh][nw] == board[h][w]:
                cnt+=1
    return cnt
