def solution(left, right):
    answer=0
    for i in range(left,right+1):
        cnt=0
        for d in range(1,i+1):
            if i%d==0:
                cnt+=1
        if cnt%2==0:
            answer+=i
        else:
            answer-=i
    return answer
