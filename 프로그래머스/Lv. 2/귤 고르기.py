def solution(k, tangerine):
    dic={}
    cnt=0
    for i in tangerine:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    lst=sorted(dic.items(), key=lambda item:item[1],reverse=True)
    for i,tup in enumerate(lst):
        #튜플 반환
        k-=lst[i][1]
        if k<=0:
            return i+1
