from collections import Counter 
def solution(participant, completion):
    answer = ''
    p=Counter(participant)
    c=Counter(completion)
    answer=p-c
    return list(answer.keys())[0]
