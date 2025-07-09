import math

def solution(n,a,b):
    if a>b:
        a,b=b,a

    result=int(math.log2(n))
    left,right=1,n

    while True:
        mid=(left+right)//2
        #<>
        if (a>=left and a<=mid) and (b>mid and b<=right):
            return result
        #<
        if (a>=left and a<=mid) and (b>=left and b<=mid):
            right=mid
        #>
        else:
            left=mid+1
            
        result-=1
