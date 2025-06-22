def solution(s):
    dic={}
    result=[]
    for i,v in enumerate(s):
        if v not in dic:
            dic[v]=i
            result.append(-1)
        else:
            result.append(i-dic[v])
            dic[v]=i
    return result
