N,K=map(int,input().split())
arr=list(map(int,input().split()))
hap=0
for i in arr:
    hap+=i
hap=hap*2-1

if 0<=K<=hap:
    arr[0]-=1
    arr[-1]+=1
    for i in range(len(arr)):
        K-=arr[i]
        if K<=0:
            result=i+1
            break
    if K>0:
        arr[0]+=2
        arr[-1]-=2
        for i in range(len(arr)-1,-1,-1):
            K-=arr[i]
            if K<=0:
                result=i+1
                break
    print(result)
