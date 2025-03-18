def solution(today, terms, privacies):
    answer = []
    
    # terms_time 
    terms_time = {}
    
    # today 쪼개기
    today_lst = today.split('.')
    today_time = int(today_lst[0]) * 12 * 28 + int(today_lst[1]) * 28 + int(today_lst[2])
    
    # terms 쪼개기 
    for term in terms:
        key, value = term.split()
        terms_time[key] = int(value) * 28  
    
    # privacies 쪼개기 
    for idx, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        year, month, day = map(int, date.split('.'))  
        
        #날먹 시간 더하기
        privacy_time = year * 12 * 28 + month * 28 + day
        
        #만료
        expiry_time = privacy_time + terms_time[term_type]
        
        #파기
        if today_time >= expiry_time:
            answer.append(idx + 1)  #result값이 1 더해야하는 문제임.
    
    return answer
