def solution(storey):
    cnt=0
    carry=0
    lst=list(map(int,str(storey)))
    for i in range(len(lst)-1,-1,-1):  
        num=lst[i]+carry
        if num<5:
            cnt+=num
            carry=0
        elif num>5:
            cnt+=(10-num)
            carry=1
        else:
            #num==5
            if i>0 and lst[i-1]>=5:
                cnt+=(10-num)
                carry=1
            else:
                cnt+=num
                carry=0
    if carry==1:
        cnt+=1
    return cnt
