///73.3 짜리 정답임. O(N*M)의 시간복잡도를 지녀서 다른 방법이 필요.
def solution(X, Y):
    answer = []
    
    for i in X:
        if i in Y:  
            answer.append(i)
            Y = Y.replace(i, "", 1)  
    
    #일치안하는 경우
    if not answer:  
        return "-1"
    
    # 하나의 0 반환
    if all(i == '0' for i in answer):
        return "0"

    # 내림차순으로 정렬
    answer = sorted(answer, reverse=True)
    return ''.join(answer)
