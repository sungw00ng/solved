def solution(word):
    words=['A','E','I','O','U']
    answer=0
    def dfs(string):
        nonlocal answer
        answer+=1
        if string==word:
            return True
        
        elif len(string)==5:
            return False
        
        for i in words:
            if dfs(string+i):
                return True
    
    for i in words:
        if dfs(i):
            return answer
