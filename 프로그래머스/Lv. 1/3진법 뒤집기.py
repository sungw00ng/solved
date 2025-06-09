def solution(n):
    lst=[]
    hap=0
    cnt=0
    while n>0:
        lst.append(n%3)
        n=n//3 
    
    for i in range(len(lst)-1,-1,-1):
        hap+=lst[i]*(3**cnt)
        cnt+=1
    return hap
