def solution(X, Y):
    answer = []
    
    for i in X:
        if i in Y:  
            answer.append(i)
            Y = Y.replace(i, "", 1)  
            """
            break는 반례가 존재해서 replace 써야됨.
            """
    
    #일치안하는 경우
    if not answer:  
        return "-1"
    
    # 하나의 0 반환
    if all(i == '0' for i in answer):
        return "0"

    # 내림차순으로 정렬
    answer = sorted(answer, reverse=True)
    return ''.join(answer)
