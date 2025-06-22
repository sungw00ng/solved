def solution(arr):
    arr1=sorted(arr)
    arr.remove(arr1[0])
    
    if not arr:
        return [-1]
    else:
        return arr
