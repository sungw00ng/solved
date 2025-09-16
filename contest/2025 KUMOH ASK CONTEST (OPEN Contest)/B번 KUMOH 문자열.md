## KUMOH 문자열
https://www.acmicpc.net/problem/34324 <br>

```text
문제 설명이 친절했다.
N개의 행과 문자열의 열은 1000으로 고정되어 있고,
입력 문자열이 짧으면 오른쪽을 ' ' 공백으로 채워서 1000자 길이로 맞춰야 한다.

(i,j)에 위치한 경우 (i-1,j+1), 즉 오른쪽 위 대각선
정방향과 역방향에서 "KUMOH"를 찾는 문제이다.

max(정방향개수,역방향개수)가 Bt가 되므로 B1+B2+...+Bk를 더해
총등장 횟수 answer를 계산하면된다.

이때까지는 백준 1193번 분수찾기의 대각선 문제와 비슷한데
여기서 빈 문자열 또한, 대각선에 포함되지만 공백은 포함하지 않고 스킵해야한다.

따라서, (K,' ',U,M,O,H)를
잘 구현하는 것이 핵심이었다.
```

```python3
n=int(input())
bound=[] #영역
answer=0 #결과
##def count_5
def count_5(s,chs):
    cnt=0
    m=len(chs)
    i=0
    while i<=len(s)-m:
        if s[i:i+m]==chs:
            cnt+=1
            i+=m
        else:
            i+=1
    return cnt

for _ in range(n):
    s=input()
    row=[s[i] if i<len(s) else ' ' for i in range(1000)]
    bound.append(row)
for i in range(n):
    row,col=i,0
    ch_lst=[]
    while row>=0 and col<1000:
        ch=bound[row][col]
        if ch!=' ':
            ch_lst.append(ch)
        row-=1 #i-1
        col+=1 #j+1
    chs=''.join(ch_lst)
    if len(chs)>=5:
        x=count_5(chs,"KUMOH") #count_5
        y=count_5(chs[::-1],"KUMOH") #count_5
        answer+=max(x,y)
        
for i in range(1,1000):
    row,col=n-1,i
    ch_lst=[]
    while row>=0 and col<1000:
        ch2=bound[row][col]
        if ch2 != ' ':
            ch_lst.append(ch2)
        row-=1
        col+=1
    chs2=''.join(ch_lst)
    if len(chs2)>=5:
        x=count_5(chs2,"KUMOH") #count_5
        y=count_5(chs2[::-1],"KUMOH") #count_5
        answer+=max(x,y)
print(answer)
```
