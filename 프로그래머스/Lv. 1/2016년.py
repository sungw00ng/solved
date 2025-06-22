def solution(a, b):
    #2016년 1월 1일 금요일, 2월은 29일까지
    days=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month_days=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    total_days = sum(month_days[:a-1])+b-1  
    return days[total_days%7]
