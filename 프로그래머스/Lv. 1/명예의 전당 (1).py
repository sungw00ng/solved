def solution(k, score):
    result=[]
    stack=[]
    for i in score:
        stack.append(i)
        stack.sort(reverse=True)
        if len(stack)==k+1:
            stack.pop()
        result.append(stack[-1])
    return result
