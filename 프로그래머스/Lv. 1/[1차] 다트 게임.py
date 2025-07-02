def solution(dartResult):
    dic={'S':1,'D':2,'T':3}
    result=[]
    s=list(dartResult)
    for i,v in enumerate(s):
        if v in dic:
            if s[i-2].isdigit() and s[i-1].isdigit():
                result.append(10**int(dic[v]))
            elif s[i-1].isdigit():
                result.append(int(s[i-1])**int(dic[v]))
        elif v=='*':
            if len(result)==1:
                result[-1]=result[-1]*2
            else:
                result[-1]=result[-1]*2
                result[-2]=result[-2]*2
                
        elif v=='#':
            result[-1]=result[-1]*(-1)
    print(result)
    return sum(result)
