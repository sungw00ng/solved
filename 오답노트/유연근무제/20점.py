#오늘부터 일주일 동안 각자 설정한 출근 희망 시각에 늦지 않고 출근한 직원들에게 상품을 주는 이벤트
#출근 희망 시각이 9시  58분인 직원은 10시 8분까지 출근해야한다.(출근희망시각~+10)
#단 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다.
#직원들이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원은 몇 명인가?
def solution(schedules, timelogs, startday):
    #schedules 출근희망시각 1차원 정수 배열 1<n<=1000
    #timelogs 일주일동안 출근한 시각 2차원 정수 배열 600<=n<=2359
    #startday 이벤트를 시작한 요일 1<=n<=7
    answer = 0
    for i,log in zip(schedules,timelogs):
        flag=True
        for eventday in range(startday-1,5): 
            if not (600<=log[eventday]<=i+10):  
                flag=False   
                break
        if flag:
            answer+=1
    return answer
