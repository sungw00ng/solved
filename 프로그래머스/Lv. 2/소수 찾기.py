from itertools import permutations
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer=set()
    
    for r in range(1,len(numbers)+1):
        PE=permutations(list(numbers),r)
        for p in PE:
            str2num="".join(p)
            if str2num.startswith('0'):
                continue
            answer.add(int(str2num))
    cnt=0
    for num in answer:
        if is_prime(num):
            cnt+=1
    return cnt
