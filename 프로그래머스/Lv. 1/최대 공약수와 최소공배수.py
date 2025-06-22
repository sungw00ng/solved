def solution(n, m):
    if n>=m:
        mx,mn=n,m
    else:
        mx,mn=m,n
    for i in range(1,mn+1):
        if mn%i==0 and mx%i==0:
            gcd=i
    gcm=gcd*(mn//gcd)*(mx//gcd)
    return [gcd,gcm]
