def solution(arr1, arr2):
    answer=[]
    result=[]
    for i,j in zip(arr1,arr2):
        for a,b in zip(i,j):
            answer.append(a+b)
        result.append(answer)
        answer=[]
    return result
