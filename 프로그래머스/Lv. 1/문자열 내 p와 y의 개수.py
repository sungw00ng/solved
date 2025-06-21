def solution(s):
    dic={'p':0,'y':0,'P':0,'Y':0}
    for i in s:
        if i in dic:
            dic[i]+=1
    if (dic['p']+dic['P']) == (dic['y']+dic['Y']):
        return True
    else:
        return False
