def solution(progresses, speeds):
    flag=[False]*len(progresses)  
    days=[0]*len(progresses)     
    
    while True:
        for i,v in enumerate(progresses):
            if not flag[i]: 
                progresses[i]+=speeds[i]  
                days[i]+=1  
                
                if progresses[i]>=100:  
                    flag[i]=True 
                    
        if all(flag):
            break
    
    
    result=[]
    count=1 
    max_index=days[0]  

    for i in range(1,len(days)):
        if days[i]<=max_index:
            count+=1 
        else:
            result.append(count)  
            count=1  
            max_index=days[i]     
    result.append(count)  

    return result
