#투포인터
def solution(n):
    ans=0
    left,right,hap=0,0,0

    while left<n:
        if hap<n:
            right+=1
            hap+=right
        else:
            if n==hap: 
                ans+=1
            
            left+=1
            hap-=left

    return ans
