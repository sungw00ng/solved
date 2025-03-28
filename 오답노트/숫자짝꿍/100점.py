def solution(X, Y):
    answer = []
    
    # 각 문자에 대해 반복하여 Y에서 제거
    for i in sorted(set(X), reverse=True):
        if i in Y:
            # X와 Y에서 공통된 최소 횟수만큼 추가
            common_count = min(X.count(i), Y.count(i))
            answer.extend([i] * common_count)
            Y = Y.replace(i, "", common_count)
    
    # 일치안하는 경우
    if not answer:
        return "-1"
    
    # 하나의 0 반환
    if all(i == '0' for i in answer):
        return "0"
    
    # 내림차순으로 정렬
    answer.sort(reverse=True)
    return ''.join(answer)
