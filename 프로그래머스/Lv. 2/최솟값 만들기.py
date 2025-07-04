def solution(A,B):
    #누적값 최소 조건: A의 최소*B의 최대
    hap=0
    A.sort()
    B.sort(reverse=True)
    for i in zip(A,B):
        hap+=i[0]*i[1]
    return hap
