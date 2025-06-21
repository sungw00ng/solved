def solution(numbers):
    hap=0
    dic={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in numbers:
        if i in dic:
            dic[i]+=1
    for i in range(0,10):
        if dic[i]==0:
            hap+=i
    return hap
