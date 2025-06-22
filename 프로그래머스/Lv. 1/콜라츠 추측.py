def solution(num):
    if num==1:
            return 0
    for i in range(1,501):
        #1-1
        if num%2==0:
            num=num//2
            if num==1:
                return i
        #1-2
        elif num%2==1:
            num=num*3+1
            if num==1:
                return i
    else:
        if num != 1:
            return -1
