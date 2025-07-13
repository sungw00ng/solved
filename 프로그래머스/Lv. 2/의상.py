def solution(clothes):
    #kind별 item
    dic={}
    
    #분류
    for item,kind in clothes:
        if kind in dic:
            dic[kind].append(item)
        else:
            dic[kind]=[item]
    
    #headgear=2
    #eyewear=1
    #01 10 00 (11은 2개 착용이므로 규칙에 어긋남) / 1 0 
    #3*2=6-1(00 0)=5
    combi=1
    for items in dic.values():
        combi*=(len(items)+1)
        
    return combi-1
