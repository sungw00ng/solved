#소수 조건
#P는 각 자릿수에 0을 포함하지 않는 소수이다.
#0P0,P0,0P,P
#예를 들어 101은 P가 될 수 없다.
#'211'0'2'01010'11'을 예시로, '211', '2', '11' 등으로 총 3개이다.
def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def solution(n, k):
    digits="0123456789ABCDEF"
    if n==0:
        return n
    nums=''
    #진법 변환
    while n>0:
        remain=n%k
        nums+=digits[remain]
        n//=k
    nums=nums[::-1]
    nums=nums.split('0')
    #print(nums)
    cnt=0
    for i in nums:
        if i: #빈 문자열 예외처리
            i=int(i)
            if prime(i):
                cnt+=1
    return cnt
