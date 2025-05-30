import sys
input=sys.stdin.readline

n,m=map(int,input().split())
train=[0]*n

for _ in range(m):
    op=list(map(int,input().split()))
    
    if op[0]==1:
        #i번째 기차, x번째 좌석
        i,x=op[1]-1,op[2]-1
        train[i]=train[i] | 1<<x
    
    elif op[0]==2:
        i,x=op[1]-1,op[2]-1
        train[i]=train[i] & ~(1<<x)
    
    elif op[0]==3:
        i=op[1]-1
        train[i]=(train[i]<<1) & ((1<<20)-1)
    
    elif op[0]==4:
        i=op[1]-1
        train[i]=train[i]>>1

print(len(set(train)))
