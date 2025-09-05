while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    lst=[input() for _ in range(n)]
    result=[['' for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if lst[i][j]=='*':
                result[i][j]='*'
            else:
                cnt=0
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if dx==0 and dy==0:
                            continue
                        ni,nj=i+dx,j+dy
                        
                        #영역 안
                        if 0<=ni<n and 0<=nj<m:
                            if lst[ni][nj]=='*':
                                cnt+=1
                result[i][j]=str(cnt)
    for i in result:
        print(''.join(i))
