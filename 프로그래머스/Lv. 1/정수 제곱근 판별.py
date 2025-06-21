def solution(n):
    answer = 0
    if (int(n**0.5)) * (int(n**0.5)) == n:
        return (int(n**0.5)+1) * (int(n**0.5)+1)
    else:
        return -1
