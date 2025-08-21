def solution(n):
    #dp[1]=1,dp[2]=2,dp[3]=3,dp[4]=5
    #fibo dp
    if n==1:
        return 1
    a,b=1,2
    for _ in range(3,n+1):
        a,b=b,a+b
    return b%1000000007
