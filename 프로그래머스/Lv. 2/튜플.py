def solution(s):
    s=s[2:-2]  
    s=s.split("},{")  
    #print(s)
    # 길이순 정렬
    sets=[list(map(int,tup.split(','))) for tup in s]
    #print(sets)
    sets.sort(key=len)
    #print(sets)
    
    result=[]
    seen=set() #중복되는 원소가 없는
    
    for i in sets:
        for num in i:
            if num not in seen:
                result.append(num)
                seen.add(num)
                #print(seen)

    return result
