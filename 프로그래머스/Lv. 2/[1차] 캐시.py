#LRU(Least Recently Used)
#hit시 뒤로, miss시 가장 오래된 페이지 비우기
def solution(cacheSize, cities):
    cache=[]
    time=0
    
    for city in cities:
        city=city.lower()  

        if cacheSize==0:
            time+=5  
            continue

        if city in cache:
            cache.remove(city)
            cache.append(city)
            time+=1  #cache hit
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)
            time+=5  #cache miss

    return time
