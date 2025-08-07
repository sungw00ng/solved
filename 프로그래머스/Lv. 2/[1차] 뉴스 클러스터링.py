from collections import Counter
def bigram(s):
    s=s.lower()
    bigram=[]
    for i in range(len(s)-1):
        pair=s[i:i+2]
        if pair.isalpha():
            bigram.append(pair)
    return bigram

def solution(str1, str2):
    a=bigram(str1)
    b=bigram(str2)
    
    #모두 공집합
    if not a and not b:
        return 1*65536
    
    #다중집합을 고려한 dict Counter
    A=Counter(a)
    B=Counter(b)
    
    #집합들
    intersection=sum((A&B).values())
    union=sum((A|B).values())
    
    #자카드 유사도
    J=intersection/union
    
    return int(J*65536)
