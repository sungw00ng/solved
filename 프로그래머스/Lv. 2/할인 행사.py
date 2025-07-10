from collections import Counter

def solution(want,number,discount):
    day=0
    want_dict=dict(zip(want,number))  
    max_length=len(discount)-10
    
    current_window=discount[:10]
    current_counter=Counter(current_window)  
    
    #true false 
    if all(current_counter.get(food,0)==want_dict[food]  \
    for food in want_dict):
        day+=1
    
    #sliding window algo(O(N)*O(1))
    for i in range(1,max_length+1):
        current_counter[discount[i-1]]-=1
        if current_counter[discount[i-1]]==0:
            del current_counter[discount[i-1]]  
        current_counter[discount[i+9]]+=1
        
        #true false 
        if all(current_counter.get(food,0)==want_dict[food] \
        for food in want_dict):
            day+=1

    return day
