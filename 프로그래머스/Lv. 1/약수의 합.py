def solution(n):
    answer = 0
    for i in range(1,int(n*(1/2))+1,1):
        if n%i==0:
            answer+=i
    answer+=n
    return answer
