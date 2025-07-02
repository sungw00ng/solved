def solution(lottos, win_nums):
    cnt=0
    cnt_0=0
    result=[]
    #1등-6개,2등-5개,3등-4개,4등-3개,5등-2개,6등-1개 이하
    for i in range(len(lottos)):
        if int(lottos[i]) in win_nums:
            cnt+=1
        if int(lottos[i])==0:
            cnt_0+=1
    high=cnt+cnt_0
    low=cnt
    if high==6:
        result.append(1)
    elif high==5:
        result.append(2)
    elif high==4:
        result.append(3)
    elif high==3:
        result.append(4)
    elif high==2:
        result.append(5)
    else:
        result.append(6)
    if low==6:
        result.append(1)
    elif low==5:
        result.append(2)
    elif low==4:
        result.append(3)
    elif low==3:
        result.append(4)
    elif low==2:
        result.append(5)
    else:
        result.append(6)
    return result
