from collections import Counter

def solution(want,number,discount):
    day=0
    want_dict=dict(zip(want,number))  
    max_length=len(discount)-10
    
    # sliding window
    for i in range(max_length+1):
        current_window=discount[i:i+10]
        current_counter=Counter(current_window)
        
        # 원하는 제품과 수량이 일치하는지 확인
        #get->있으면 w 없으면 0
        if all(current_counter.get(food,0)==want_dict[food] \
        for food in want_dict):
            day+=1
    
    return day
