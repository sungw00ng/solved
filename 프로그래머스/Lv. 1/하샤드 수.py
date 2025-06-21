def solution(x):
    hap=0
    #모든 자릿수 구하기
    lst=list(str(x))
    for i in lst:
        hap+=int(i)
        
    #나눗셈이 되는가
    if x%hap==0:
        return True
    else:
        return False
