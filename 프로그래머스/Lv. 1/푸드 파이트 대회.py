def solution(food):
    result=""
    #홀수개면 -1을 할 것
    for i in range(1,len(food)):
        if food[i]%2==1:
            food[i]-=1
        if food[i]==0:
            pass
        result+=str(i)*(food[i]//2)
    result+='0'
    for i in range(len(food)-1,0,-1):
        if food[i]==0:
            pass
        result+=str(i)*(food[i]//2)
    return result
