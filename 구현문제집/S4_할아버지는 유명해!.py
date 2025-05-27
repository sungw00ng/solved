while(True):
    #rank counting list (0~10000)
    ranking=[0]*10001 
    N,M=map(int,input().split())
    if(N==0 and M==0):
        break
    
    #계수 값 넣기    
    for _ in range(N):
        arr=map(int,input().split())
        for i in arr:
            ranking[i]+=1
    
    #2등 찾기
    first=max(ranking)
    second=0
    
    for count in ranking:
        if count != first:
            second=max(count,second)
            
    #2등 점수 출력
    result=[]
    for count in range(10001):
        if ranking[count]==second:
            result.append(count)
    print(*result)
