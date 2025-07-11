def solution(s):
    result=0
    dic={')':'(','}':'{',']':'['}

    long_s=s+s
    for i in range(len(s)):
        stack=[]
        temp=long_s[i:i+len(s)]
        valid=True
        for i in temp:
            if i in '({[':
                stack.append(i)
            elif i in ')}]':
                if not stack or stack[-1]!=dic[i]:
                    valid=False
                    break
                stack.pop()
        if valid and not stack:
            result+=1
    return result
