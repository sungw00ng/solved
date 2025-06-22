def solution(array, commands):
    result=[]
    for c in commands:
        temp=[]
        for i in range(c[0]-1,c[1]):
            temp.append(array[i])
        temp.sort()
        result.append(temp[c[2]-1])
    return result
