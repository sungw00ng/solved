def solution(land):
    answer=0
    for i in range(1,len(land)):
        for j in range(4): 
            max_prev=0
            for k in range(4):
                if k!=j:
                    if land[i-1][k]>max_prev:
                        max_prev=land[i-1][k]
            #이전 행과 더하기
            land[i][j]+=max_prev
    answer=max(land[-1])
    return answer
