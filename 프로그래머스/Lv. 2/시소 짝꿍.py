from collections import Counter
def solution(weights):
    answer=0
    c=Counter(weights)

    for i in range(100,1001):
        if c[i]>0:
            answer+=(c[i]*(c[i]-1))/2 #nC2
            answer+=c[i]*c[(i*3)/2] 
            answer+=c[i]*c[i*2] 
            answer+=c[i]*c[(i*4)/3] 

    return answer
