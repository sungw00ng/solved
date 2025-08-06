from collections import deque
def solution(maps):
    n,m=len(maps[0]),len(maps)
    visited=[[False]*n for _ in range(len(maps))]
    visited[0][0]=True
    
    moves=[(1,0),(-1,0),(0,1),(0,-1)]
    q=deque()
    q.append((1,0,0))
    
    while q:
        cnt,row,col=q.popleft()
        
        #도착 
        if row==m-1 and col==n-1:
            #print(q)
            return cnt
        
        for d_row,d_col in moves:
            next_row=row+d_row
            next_col=col+d_col
            
            if 0<=next_row<m and 0<=next_col<n and visited[next_row][next_col]==False and maps[next_row][next_col]==1:
                q.append((cnt+1,next_row,next_col))
                visited[next_row][next_col]=True
    return -1
        
            
        
    
