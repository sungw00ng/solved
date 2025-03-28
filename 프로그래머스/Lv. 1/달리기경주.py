def solution(players, callings):
    #선수 순서 "mumu": 0, "soe": 1, ... 
    #딕셔너리 내포
    player_order = {player: idx for idx, player in enumerate(players)}

    for i in callings:
        #player 순서 탐색
        index = player_order[i]
        
        if index > 0:
            # swap
            players[index], players[index - 1] = players[index - 1], players[index]
            
            #뒤이어질 for문을 위해 함께 수정
            player_order[players[index]] = index
            player_order[players[index - 1]] = index - 1

    return players
