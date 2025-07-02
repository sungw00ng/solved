def solution(N, stages):
    result={}
    total=len(stages)
    
    for stage in range(1, N + 1):
        count = stages.count(stage)  
        if total == 0:
            fail = 0
        else:
            fail=count/total
        result[stage]=fail
        total-=count   
    
    # 실패율 내림차순 -result[x], 같으면 오름차순 x
    return sorted(result, key=lambda x: (-result[x], x))
