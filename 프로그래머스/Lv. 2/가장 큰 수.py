def solution(numbers):
    numbers=list(map(str,numbers))
    #문자열 길이 보정 s*원소자릿수
    numbers.sort(key=lambda x:x*4,reverse=True)
    #000->0
    return str(int(''.join(numbers)))
