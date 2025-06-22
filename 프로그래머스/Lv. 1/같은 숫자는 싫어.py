def solution(arr):
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            arr[i-1]=-1
    return [x for x in arr if x != -1]
