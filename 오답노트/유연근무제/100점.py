'''
참고자료: 윤주한님
https://velog.io/@yoonjuhan/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EC%9C%A0%EC%97%B0%EA%B7%BC%EB%AC%B4%EC%A0%9C-Python
'''


#오늘부터 일주일 동안 각자 설정한 출근 희망 시각에 늦지 않고 출근한 직원들에게 상품을 주는 이벤트
#출근 희망 시각이 9시  58분인 직원은 10시 8분까지 출근해야한다.(출근희망시각~+10)
#단 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다.
#직원들이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원은 몇 명인가?
def convertTime(n):  # 분 단위로 변환
    return (n // 100) * 60 + (n % 100)

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        s = startday
        schedule = convertTime(schedules[i])

        for eventday in range(7):
            #주말 건너뛰기
            if s in [6, 7]: 
                s += 1
                if s == 8:  
                    s = 1
                continue

            if convertTime(timelogs[i][eventday]) > schedule + 10:  
                break
            s += 1  
            if s == 8:  
                s = 1
        else:
            answer += 1

    return answer

