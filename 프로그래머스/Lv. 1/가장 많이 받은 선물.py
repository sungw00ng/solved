def solution(friends, gifts):
    #본인에게 선물할 수 없다.
    #두 사람이 선물을 주고받은 기록이 있다면, 더 많이 선물 준 사람이 다음 달에 선물을 하나 받음.
    #두 사람이 주고받은 기록이 없거나  같다면 선물 지수가 더 큰 사람이 작은 사람에게 선물을 하나 받음.
    #만약, 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않는다.
    #선물지수=(자신이 친구들에게 준 선물 수)-(친구들이 본인에게 준 선물 수)
    #friends=친구들 이름
    #gifts=친구들이 주고 받은 선물 기록 (A:선물을 준 친구, B:선물을 받은 친구)
    #다음 달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return
    result={}
    
    #friends 초기화(dict 내포)
    giftscore = {f: 0 for f in friends}
    ab_history = {f: [] for f in friends}
    next_month_gift = {f: 0 for f in friends}
    
    # 선물 준 사람, 받은 사람 
    for i in gifts:
        sender, receiver = i.split(' ')
        ab_history[sender].append(receiver)
        #선물지수
        giftscore[sender]+=1
        giftscore[receiver]-=1
    #print(giftscore)
    
    # 리스트로 바꾸기
    for i in ab_history:
        ab_history[i] = [ab_history[i].count(user) for user in friends]
        #print(ab_history[i])
    
    #AB 비교
    for i in range(len(friends)):
        for j in range(len(friends)):
            #같으면 다음 시행
            if i == j:
                continue
            
            sender = friends[i]
            receiver = friends[j]

            send_to = ab_history[sender][j]
            receive_from = ab_history[receiver][i]

            if send_to > receive_from:
                next_month_gift[sender] += 1
            elif send_to == receive_from:
                if giftscore[sender] > giftscore[receiver]:
                    next_month_gift[sender] += 1
    return max(next_month_gift.values())
