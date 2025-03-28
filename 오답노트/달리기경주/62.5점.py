def solution(players, callings):
    for i in callings:
        if i in players:
            index = players.index(i)
            if index > 0:
                #swap
                players[index], players[index - 1] = players[index - 1], players[index]
                
    return player
