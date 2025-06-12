def solution(keymap, targets):
    answer = []
    dic={}
    
    for key in keymap:
        for idx,val in enumerate(key):
            if val in dic:
                if dic[val] >= idx+1:
                    dic[val]=idx+1
                else:
                    pass
            
            else:
                dic[val]=idx+1
    
    for t in targets:
        hap=0
        for idx,val in enumerate(t):
            if val in dic:
                hap+=dic[val]
            else:
                hap=-1
                break
        answer.append(hap)

    return answer
