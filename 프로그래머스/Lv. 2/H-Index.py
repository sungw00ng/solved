def solution(citations):
    lst=sorted(citations,reverse=True)
    #65310
    for i,v in enumerate(lst):
        #인용 수 부족 시작
        if i>=v:
            return i
    #100,90,80,70,60
    return len(lst)
