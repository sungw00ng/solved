## 일정들을 grid위에 배치하는 2차원 리스트 풀이
```python
N = int(input())
calendar = [list(map(int, input().split())) for _ in range(N)]

# 날짜 범위 파악
max_day = 0
for start, end in calendar:
    max_day = max(max_day, end)

# 날짜별 일정 수 저장
day_line = [0] * (max_day + 2)  # 1-based index

for start, end in calendar:
    for day in range(start, end + 1):
        day_line[day] += 1

# 면적 계산
total_area = 0
width = 0
height = 0

for day in range(1, max_day + 2):
    if day_line[day] > 0:
        width += 1
        height = max(height, day_line[day])
    else:
        total_area += width * height
        width = 0
        height = 0

print(total_area)
```

<br><br><br><br>

## 좀 더 그리디한 1차원 리스트 풀이
```python
N = int(input())
calendar = [list(map(int, input().split())) for _ in range(N)]

# 날짜 범위 파악
max_day = 0
for start, end in calendar:
    max_day = max(max_day, end)

# 날짜별 일정 수 저장
day_line = [0] * (max_day + 2)  # 1-based index

for start, end in calendar:
    for day in range(start, end + 1):
        day_line[day] += 1

# 면적 계산
total_area = 0
width = 0
height = 0

for day in range(1, max_day + 2):
    if day_line[day] > 0:
        width += 1
        height = max(height, day_line[day])
    else:
        total_area += width * height
        width = 0
        height = 0

print(total_area)
```
