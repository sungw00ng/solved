def solution(s):
    answer=""
    lst=list(s)
    lst.sort(reverse=True)
    for i in lst:
        answer+=i
    return answer
