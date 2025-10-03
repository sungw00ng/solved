from functools import reduce
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def solution(arrayA, arrayB):
    #1<=len(arrayA)=len(arrayB)<=500,000
    #1<=arrayA,arrayB 원소값<=100,000,000
    gcdA,gcdB=arrayA[0],arrayB[0]
    
    for i in arrayA[1:]:
        gcdA=gcd(gcdA,i)    
    for i in arrayB[1:]:
        gcdB=gcd(gcdB,i)
    
    checkA=all(i%gcdA!=0 for i in arrayB)
    checkB=all(i%gcdB!=0 for i in arrayA)

    answer=0
    if checkA:
        answer=gcdA
    if checkB:
        answer=max(answer,gcdB)

    return answer
