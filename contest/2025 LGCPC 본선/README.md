## 대회일자
- 25.9.20 14:00~17:00 <br>

## 문제
- A - 교도소 <br>
- B - ABX <br>
- C - 매직 리그 <br>
- D - 배달 <br>

## 참가 후기
```text
문제들이 대기업 코테를 아득히 뛰어넘는 수준이 문제들이었다..
교도소 한 문제를 부분 점수를 받았다.
각 수감인원이 10억명이다보니
시간복잡도를 줄이는 방법을 고려해야했다.
한참을 고민하다가 투포인터를 사용하였음에도
이 이상 나아가는 방법을 찾지 못했다.
```

## A 교도소 부분 풀이
```python3
import sys
input=sys.stdin.readline
n=int(input())
rooms=list(map(int, input().split()))
avg=sum(rooms)//n
none=[]
answer=0
front=[]
back=[]

for i in range(n):
    diff=rooms[i]-avg
    none.append(diff)
    if diff>0:
        front.append((i,diff))
    elif diff<0:
        back.append((i,-diff))

#투포인터
i,j=0,0
front_count=front[i][1] if front else 0
back_count=back[j][1] if back else 0

while i<len(front) and j<len(back):
    # 현재 매칭할 양
    match=min(front_count,back_count)
    
    # 이동 거리 계산 (단방향)
    f_idx=front[i][0]
    b_idx=back[j][0]
    
    if f_idx<=b_idx:
        moves=b_idx-f_idx
    else:
        moves=n-f_idx+b_idx
    
    answer+=(match*moves)
    
    #업데이트
    front_count-=match
    back_count-=match
    
    #다음 이동
    if front_count==0:
        i += 1
        if i<len(front):
            front_count=front[i][1]
    
    if back_count==0:
        j+=1
        if j<len(back):
            back_count=back[j][1]

print(answer)
```  
