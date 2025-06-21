def solution(n):
    answer = 0
    for i in range(2,n+1,1):
        flag=True
        
        for v in range(2,int(i**(1/2)+1),1):
            if i%v==0:
                flag=False
                break
        if flag:
            answer+=1
    return answer
