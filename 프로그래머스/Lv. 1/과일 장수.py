def solution(k, m, score):
    #최저 사과 점수 * 한 상자에 담긴 사과 개수 * 상자의 개수
    #k=최대 점수, m=한 상자에 들어가는 사과 수
    stack=[]
    answer=0
    score.sort(reverse=True)
    for i in range(len(score)):
        stack.append(score[i])
        if len(stack)%m==0:
            answer+=min(stack)*m
            stack=[]

    return answer
