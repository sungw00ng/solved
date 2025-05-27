N=int(input())           
target=int(input())      

map_=[[0]*N for _ in range(N)]  
x=y=0         

#DRUL
dx=[1,0,-1,0] 
dy=[0,1,0,-1] 

dir=0   
value=N*N                 
target_x=target_y=0     

#초기배열
visited=[[False]*N for _ in range(N)]

#달팽이 돌리기
for _ in range(N*N):
    map_[x][y]=value
    visited[x][y]=True
    if value==target:
        target_x=x+1
        target_y=y+1
    value-=1 

    #next
    nx=x+dx[dir]
    ny=y+dy[dir]

    #except
    if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]:
        dir=(dir+1)%4
        nx=x+dx[dir]
        ny=y+dy[dir]

    x=nx
    y=ny

#출력
for row in map_:
    print(*row)


print(target_x,target_y)
