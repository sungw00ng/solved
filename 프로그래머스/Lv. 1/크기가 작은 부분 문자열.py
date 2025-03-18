def solution(t, p):
    answer=0
    p_len=len(p)
    t_len=len(t)
    lt=len(t)
    lp=len(p)
    for i in range(0,t_len-p_len+1):
        if(int(t[i:p_len+i]) <= int(p)):
            answer+=1
    return answer
