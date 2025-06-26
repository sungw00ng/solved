from itertools import combinations
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
    
def solution(nums):
    result=0
    hap=[sum(x) for x in combinations(nums,3)]
    for i in hap:
        result+=is_prime(i)

    return result
