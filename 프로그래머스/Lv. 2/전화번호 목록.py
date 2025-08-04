def solution(phone_book):
    dic={}
    for i in phone_book:
        dic[i]=1
    for i in phone_book:
        temp=""
        for char in i[:-1]: #자기자신제외
            temp+=char
            if temp in dic:
                return False
    return True
