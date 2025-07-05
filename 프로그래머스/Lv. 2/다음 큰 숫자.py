def solution(n):
    #n의 다음 큰 숫자는 자연수
    #n의 다음 큰 숫자와 n을 각각 2진수 변환 시 1의 개수가 같음
    #n의 다음 큰 숫자는 조건,1,2를 만족하는 수 중 가장 작은 수
    result=n+1
    t=bin(n)
    t_cnt=t.count('1')
    
    while True:
        if bin(result).count('1')==t_cnt:
            break
        
        result+=1
    return result
