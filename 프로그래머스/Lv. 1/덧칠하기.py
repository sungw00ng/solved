def solution(n, m, section):
    cnt=0
    i=0
    lst=[True]*n
    for i in section:
        lst[i-1]=False
    for i,v in enumerate(lst):
        if v==False:
            cnt+=1
            if i+m-1<n:
                lst[i:i+m]=[True]*m
            else:
                lst[i:]=[True]*(n-i)
    return cnt
