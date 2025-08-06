from collections import deque
#숫자가 클수록 가장 빨리 꺼낸다
def solution(priorities, location):
    result=0
    process=deque(priorities)
    prior=deque(priorities)
    process[location]=-1
    
    while process:
        process_target=process.popleft()
        prior_target=prior.popleft()
        
        #내가 꺼내려는 문서보다 우선순위가 더 높은 문서가 없는 경우 break
        if process_target==-1 and (not prior or max(prior)) <= prior_target:
            result+=1
            break
        #한 번 실행한 프로세스는 다시 큐에 안넣고 종료
        elif process_target>=max(prior):
            result+=1
            
        # 우선순위가 더 높은 프로세스가 있다면 다시 큐에 넣기
        elif process_target<max(prior):
            process.append(process_target)
            prior.append(prior_target)
    return result
