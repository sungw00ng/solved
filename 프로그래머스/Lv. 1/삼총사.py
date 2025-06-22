def solution(number):
    count=0  
    nums=number
    n=len(nums)
    
    def nCr(idx, selected):
        nonlocal count
        if len(selected)==3:
            if sum(selected)==0:
                count+=1
            return
        if idx==n:
            return
        
        # 현재 인덱스 선택
        selected.append(nums[idx])
        nCr(idx+1,selected)
        selected.pop()
        
        # 선택안할 때
        nCr(idx+1,selected)
    
    nCr(0,[])
    return count
