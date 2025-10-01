def solution(book_time):
    #청소 시간 뒤에 예약시간이 가장 가까운 대실 시간 배치
    #가장 길수록 따로 배치
    #00:00~23:59 / 0 ~ (23*60)+59
    lst=[]
    rooms=[]
    for s,e in book_time:
        lst.append([int(s[:2])*60+int(s[-2:]), \
        int(e[:2])*60+int(e[-2:])+10]) 
    lst.sort()
    #print(lst)
    for s,e in lst:
        for i in range(len(rooms)):
            if rooms[i]<=s:
                rooms[i]=e
                break
        #for-else
        else:
            rooms.append(e)
            rooms.sort()
    return len(rooms)
