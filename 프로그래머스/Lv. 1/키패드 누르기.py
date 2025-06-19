def solution(numbers, hand):
    answer=''
    l='*'
    r='#'
    dic={
        1:(0,0),
        2:(0,1),
        3:(0,2),
        4:(1,0),
        5:(1,1),
        6:(1,2),
        7:(2,0),
        8:(2,1),
        9:(2,2),
        '*':(3,0),
        0:(3,1),
        '#':(3,2)
    }
    #left왼손잡이 / right오른손잡이
    # 123
    # 456
    # 789
    # *0#
    for i in numbers:
        if i==1 or i==4 or i==7:
            answer+='L'
            l=i
        elif i==3 or i==6 or i==9:
            answer+='R'
            r=i
        #대각선 이동 X
        else:
            l_size=abs(dic[i][0]-dic[l][0])+abs(dic[i][1]-dic[l][1])            
            r_size=abs(dic[r][0]-dic[i][0])+abs(dic[i][1]-dic[r][1])
            if l_size>r_size:
                answer+='R'
                r=i
            elif l_size<r_size:
                answer+='L'
                l=i
            else:
                if hand=="right":
                    answer+='R'
                    r=i
                elif hand=="left":
                    answer+='L'
                    l=i
                    
    return answer
