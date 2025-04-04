def solution(ingredient):
    #1-빵, 2-야채, 3-고기
    #1-2-3-1 ->햄버거 하나
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:  
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    return answer
