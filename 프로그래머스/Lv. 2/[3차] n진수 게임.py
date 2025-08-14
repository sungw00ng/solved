def solution(n, t, m, p):
    #0,/1,/1,0,/1,1,/1 
    #진법n,미리구할숫자개수t,인원m,튜브순서p(p는 말해야되는 사람)
    #이진법부터 십육진법까지 모든 진법으로 가능해야함
    result=''
    진법변환완료='0'
    over10={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    #t*m:순번 전체 문자,진법 변환
    for i in range(1,t*m):
        num=''
        while i>0:
            div=i%n #나머지로 가장 오른쪽부터 채우기
            if div>=10:
                div=over10[div]
            num+=str(div) #문자열 저장
            i=i//n #다음 나누기를 위함(순서 돌리기)
        진법변환완료+=num[::-1]
    
    #0-based, (p-1),(p-1)+m, (p-1)+m+m
    for i in range(p-1,len(진법변환완료),m):
        result+=진법변환완료[i]
    
    #t까지말해야함
    return result[:t]
