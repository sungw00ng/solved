def solution(babbling):
    result=0
    word=["aya","ye","woo","ma"]
    for i in babbling:
        for w in word:
            i = i.replace(w,w+' ')
            
        lst=i.strip().split(' ')
        flag=True
        
        for i,v in enumerate(lst):
            if v not in word:
                flag=False
                break
            else:
                if i>=1:
                    if lst[i]==lst[i-1]:
                        flag=False
                        break
        if flag:
            result+=1
    return result
            
        
        
