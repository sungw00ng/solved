def solution(data, ext, val_ext, sort_by):
    answer = []
    
    for i in data:
        if ext=="date":
            if i[1]<val_ext:
                answer.append(i)
        elif ext=="code":
            if i[0]<val_ext:
                answer.append(i)
        elif ext=="maximum":
            if i[2]<val_ext:
                answer.append(i)
        elif ext=="remain":
            if i[3]<val_ext:
                answer.append(i)
    
    if sort_by=="code":
        answer=sorted(answer,key=lambda x:x[0])
    
    elif sort_by=="date":
        answer=sorted(answer,key=lambda x:x[1])
        
    elif sort_by=="maximum":
        answer=sorted(answer,key=lambda x:x[2])
    
    elif sort_by=="remain":
        answer=sorted(answer,key=lambda x:x[3])
    
            
    return answer
