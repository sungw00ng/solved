def solution(cards1, cards2, goal):
    answer='Yes'
    cards1_cnt=[]
    cards2_cnt=[]

    for v in goal:
        if v in cards1:
            cards1_cnt.append(cards1.index(v))
        elif v in cards2:
            cards2_cnt.append(cards2.index(v))

    if not all(idx == cnt for idx, cnt in enumerate(cards1_cnt)) or  \
    not all(idx == cnt for idx, cnt in enumerate(cards2_cnt)):
        answer = "No"

    return answer
