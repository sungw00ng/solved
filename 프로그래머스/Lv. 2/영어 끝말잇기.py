import math 
def solution(n, words):
    #[player num,turn]
    watched=[]
    for i,v in enumerate(words):
        if v in watched:
            a=i+1
            person=a%n if a%n!=0 else n
            turn=math.ceil(a/n)
            return [person,turn]
        elif len(watched)>=1: 
            if v[0] != watched[-1][-1]:
                a=i+1
                person=a%n if a%n!=0 else n
                turn=math.ceil(a/n)
                return [person,turn]
        watched.append(v)
    return [0,0]
