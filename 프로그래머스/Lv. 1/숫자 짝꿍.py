def solution(X, Y):
    X = str(X)
    Y = str(Y)
    answer = []
    
    #작은 문자열 찾기
    small, large = (X, Y) if len(X) <= len(Y) else (Y, X)
    
    for i in small:
        if i in large:
            answer.append(i)
            # 한 번만 제거
            large = large.replace(i, "", 1)  
            """
            break쓰면 될 것 같지만 .. ? 반례가 존재했음.
            """

    if not answer:
        return "-1"

    #내림차순
    answer = sorted(answer, reverse=True)
    
    # 0이 여러 개일 경우 하나의 "0"만 반환하도록 처리
    if answer[0] == "0":
        return "0"
    
    return ''.join(answer)
