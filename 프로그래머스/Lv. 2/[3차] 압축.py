def solution(msg):
    answer=[]
    lst=[i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    max_len,move_len=1,1
    while msg:
        if msg[0:move_len] in lst:
            answer.append(lst.index(msg[:move_len])+1) 
            lst.append(msg[:move_len+1]) #사전 추가
            msg=msg[move_len:] #제거
            max_len=(move_len+1) if move_len+1 > max_len else max_len #갱신
            move_len=max_len #최대길이부터 재탐색
        else:
            move_len-=1
    return answer
