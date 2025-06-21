def solution(absolutes, signs):
    result=0
    for i,flag in zip(absolutes,signs):
        if flag:
            result+=i
        else:
            result-=i
    return result
        
