def solution(n):
    #1->(1) 1
    #2->(2),(1,1) 2
    #3->(1,2),(2,1),(1,1,1) 3
    #4->(2,2),(1,1,2),(1,2,1),(2,1,1),(1,1,1,1) 5
    dp=[0]*(n+1)
    dp[0]=1  
    for i in range(1,n+1):
        #fibo
        for num in [1,2]:
            if i-num>=0:
                dp[i]+=dp[i-num]
    return dp[n]%1234567
