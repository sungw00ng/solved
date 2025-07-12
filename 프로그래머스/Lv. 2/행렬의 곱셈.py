def solution(arr1, arr2):
    result=[]
    for i in range(len(arr1)):
        row=[]
        for j in range(len(arr2[0])):
            val=0
            for k in range(len(arr2)):
                val+=arr1[i][k]*arr2[k][j]
            row.append(val)
        result.append(row)
    return result
