N=int(input())
problem = [list(input()) for _ in range(N)]
present = [list(input()) for _ in range(N)]
mine_ox=False
direction=[(1,-1), (1,0),  (1,1),
           (0,-1),         (0,1),
           (-1,-1),(-1,0),(-1,1)]

#지뢰 눌렀는지 안눌렀는지
for i in range(N):
    for j in range(N):
        if present[i][j]=='x':
            if problem[i][j]=='*':
                mine_ox=True

#전체 '*' 공개
if mine_ox:
    for i in range(N):
        for j in range(N):
            if problem[i][j]=='*':
                present[i][j]='*'
            #cnt
            elif present[i][j]=='x':
                cnt=0
                for row,col in direction:
                    #direct
                    nx,ny=i+row,j+col
                    if 0<=nx<N and 0<=ny<N:
                        if problem[nx][ny]=='*':
                            cnt+=1
                present[i][j]=str(cnt)
            else:
                present[i][j]='.'
#'x'인 칸만 주변 지뢰 개수 보여주고, 나머지는 '.'
else:
    for i in range(N):
        for j in range(N):
            #cnt
            if present[i][j]=='x':
                cnt=0
                for row,col in direction:
                    #direct
                    nx,ny=i+row,j+col
                    if 0<=nx<N and 0<=ny<N:
                        if problem[nx][ny]=='*':
                            cnt+=1
                present[i][j]=str(cnt)
            else:
                present[i][j]='.'
for row in present:
    print(''.join(row))
