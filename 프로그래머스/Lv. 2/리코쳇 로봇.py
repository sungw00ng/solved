def bfs(start,end,board):
    rows,cols=len(board),len(board[0])
    visited=[[False]*cols for _ in range(rows)]
    visited[start[0]][start[1]]=True
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    queue=[(start[0],start[1],0)]
    
    while queue:
        x,y,cnt=queue.pop(0)
        
        if (x,y)==end:
            return cnt
        
        for dx,dy in moves:
            nx,ny=x,y
            
            #slide
            while True:
                tx,ty=nx+dx,ny+dy
                if 0<=tx<rows and 0<=ty<cols and \
                board[tx][ty]!='D':
                    nx,ny=tx,ty
                else:
                    break
            
            if not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny,cnt+1))
    return -1

def solution(board):
    start=end=None
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='R':
                start=(i,j)
            elif board[i][j]=='G':
                end=(i,j)
    return bfs(start,end,board)
