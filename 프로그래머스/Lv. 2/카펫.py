def solution(brown, yellow):
    n=brown+yellow
    lst=[]
    for i in range(1,int(n**0.5)+1):
        #순서쌍
        if n%i==0:
            j=n//i
            if 2*(i+j)-4==brown:
                return [j,i]
