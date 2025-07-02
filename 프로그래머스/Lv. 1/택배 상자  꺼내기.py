def solution(n, w, num):
    answer=0 
    h=n//w+1      #높이
    x=1           #상자번호
    storage=[]    #창고
    
    for i in range(h):
        t=[]
        for j in range(w):
            #n보다 작은 상자들
            if x<=n:  
                t.append(x)
                x+=1
            #n보다 큰 빈 공간은 0으로
            else:       
                t.append(0)
        
        #정방향 라인
        if i%2==0:  
            storage.append(t)
        #역방향 라인
        else:           
            t.reverse()
            storage.append(t)
            
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j]==num:
                d=i
                while d<h and storage[d][j]:    
                    answer+=1
                    d+=1	
    
    return answer
