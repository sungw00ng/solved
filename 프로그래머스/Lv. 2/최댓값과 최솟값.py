def solution(s):
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=int(s[i])
    return f"{min(s)} {max(s)}"
