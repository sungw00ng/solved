def solution(name, yearning, photo):
    dic={}
    answer=[]
    for idx,val in enumerate(name):
        dic[val]=yearning[idx]
            
    for i in photo:
        hap=0
        for j in i:
            if j in dic:
                hap+=dic[j]
        answer.append(hap)
                
    return answer
