from collections import Counter

def solution(topping):
    result=0
    left=set()
    right=Counter(topping)  
    
    for t in topping:
        left.add(t)            
        right[t]-=1          
        if right[t]==0:
            del right[t]      
        if len(left)==len(right):
            result+=1
    return result
