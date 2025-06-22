def solution(s, n):
    result=""
    s=list(s)
    for i in s:
        if i==' ':
            result+=i
            
        elif 65<=ord(i)<=90:
            if 65<=ord(i)+n<=90:
                result+=chr(ord(i)+n)
            else:
                result+=chr( (ord(i)+n-65)%26 +65)
        elif 97<=ord(i)<=122:
            if 65<=ord(i)+n<=90:
                result+=chr(ord(i)+n)
            else:
                result+=chr( (ord(i)+n-97)%26 +97 )
    return result
