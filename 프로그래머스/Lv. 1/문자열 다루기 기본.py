def solution(s):
    if len(s)==4 or len(s)==6:
        for i in s:
            if 65<=ord(i)<=90 or 97<=ord(i)<=122:
                return False
        return True
    else:
        return False
