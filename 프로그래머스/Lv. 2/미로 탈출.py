def bfs(start,end,maps):
    rows,cols=len(maps),len(maps[0])
    visited=[[False]*cols for _ in range(rows)]
    visited[start[0]][start[1]]=True
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    queue=[(start[0],start[1],0)]
    
    while queue:
        x,y,cnt=queue.pop(0)
        
        if (x,y)==end:
            return cnt
    
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and \
            maps[nx][ny]!='X' and \
            not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny,cnt+1))
    return -1

def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                start=(i,j)
            elif maps[i][j]=='L':
                lever=(i,j)
            elif maps[i][j]=='E':
                end=(i,j)
    
    bfs_lever=bfs(start,lever,maps)
    if bfs_lever==-1:
        return -1
    bfs_end=bfs(lever,end,maps)
    if bfs_end==-1:
        return -1
    return bfs_lever+bfs_end
