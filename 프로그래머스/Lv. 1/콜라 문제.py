def solution(a, b, n):
    cnt=0
    #a=콜라 b개당 줘야하는 빈 병, b=주는 콜라개수, 빈 병 n개, 1<=b<a<=n
    while True:
        if(n<a):
            break
        받은_콜라=(n//a)*b
        cnt+=받은_콜라
        n=n%a
        n+=받은_콜라
    return cnt
