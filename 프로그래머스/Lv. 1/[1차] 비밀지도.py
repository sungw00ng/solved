def solution(n, arr1, arr2):
    result=[]
    #매개변수 인덱스
    for i1,i2 in zip(arr1,arr2):
        temp1=""
        temp2=""
        temp=""
        #매개변수 인덱스 하나당 2진법 처리
        for v in range(n-1,-1,-1):
            #arr1
            if i1>=2**v:
                i1-=2**v
                temp1+='#'
            else:
                temp1+=' '
            #arr2
            if i2>=2**v:
                i2-=2**v
                temp2+='#'
            else:
                temp2+=' '
        #temp
        for j1,j2 in zip(temp1,temp2):
            if j1=='#' or j2=='#':
                temp+='#'
            elif j1==' ' and j2==' ':
                temp+=' '
        result.append(temp)
    return result
