def solution(elements):
    lst=elements+elements
    result=[]
    for i in range(0,len(elements)):
        for j in range(len(elements)):
            result.append(sum(lst[j:j+i+1]))
    return len(set(result))
