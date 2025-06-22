def solution(a, b):
    hap=0
    for a,b in zip(a,b):
        hap+=a*b
    return hap
