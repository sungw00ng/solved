def solution(n):
    lst=list(str(n))
    lst.sort(reverse=True)
    a=''
    for i in lst:
        a+=i
    a=int(a)
    return a
