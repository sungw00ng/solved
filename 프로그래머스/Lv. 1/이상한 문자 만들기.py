def solution(s):
    s=s.split(' ')
    answer=''
    print(s)
    for idx,i in enumerate(s):
        for j in range(len(i)):
            if j%2==0:
                answer+=i[j].upper()
            else:
                answer+=i[j].lower()
        if idx != len(s)-1:
            answer+=' '
    return answer
