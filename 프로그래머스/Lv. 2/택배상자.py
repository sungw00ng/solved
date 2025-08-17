def solution(order):
    answer=0
    container=[]
    order=order[::-1]   
    
    for i in range(1, len(order) + 1):
        container.append(i)
        while container and order and container[-1]==order[-1]:
            container.pop()
            order.pop()
            answer+=1
    return answer
