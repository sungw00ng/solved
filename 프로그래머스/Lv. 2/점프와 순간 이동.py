def solution(n):
    cnt=0
    while n>0:
        if n%2==1:
            cnt+=1
            n-=1
            if n==0:
                return cnt
        else:
            n/=2
            
    return cnt 
