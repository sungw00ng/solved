import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
arr=list(map(int,input().split()))

total=0
products=[0]*N

#품질점수
for i in range(N):
    a=arr[i%N]
    b=arr[(i+1)%N]
    c=arr[(i+2)%N]
    d=arr[(i+3)%N]
    prod=a*b*c*d
    products[i]=prod
    total+=prod
    
joke=list(map(int,input().split()))

#욱제의 장난
for j in joke:
    idx=j-1
    for offset in range(4):
        prod_idx=(idx-offset+N)%N
        total-=products[prod_idx]
        
        products[prod_idx]*=-1
        total+=products[prod_idx]
    print(total)
