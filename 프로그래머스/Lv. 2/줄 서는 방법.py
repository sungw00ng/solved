import math
def solution(n,k):
    lst=list(range(1,n+1))
    answer=[]
    k-=1
    for i in range(n):
        fact=math.factorial(n-1-i)
        idx=k//fact
        answer.append(lst.pop(idx))
        k%=fact
    return answer
