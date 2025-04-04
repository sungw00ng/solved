def solution(nums):
    unique=set(nums)
    answer=min((len(nums)/2),len(unique))
    return answer
