def solution(k, dungeons):
    n=len(dungeons)
    max_count=0
    visited=[False]*n
    
    def dfs(hp,count):
        nonlocal max_count
        max_count=max(count,max_count)
        for i in range(n):
            min_r,cost=dungeons[i]
            #가지치기
            if hp>=min_r and not visited[i]:
                visited[i]=True
                dfs(hp-cost,count+1)
                visited[i]=False
    dfs(k,0)
    return max_count
