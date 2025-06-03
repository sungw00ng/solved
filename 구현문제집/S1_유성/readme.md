## try 1
- 우선 보자마자 전치행렬이 떠올랐다.
- 열 기준으로 정렬한 뒤, .과 X개수만 세서 바꾸면되겠다 생각이 들어서,
- 퀵 정렬의 분할 코드를 썼는데 오답이 나왔다.
```python
R, S=map(int, input().split())
matrix=[list(input()) for _ in range(R)]

#전치행렬
col_matrix=list(map(list,zip(*matrix)))

for i in range(S):
    col=col_matrix[i]
    if '#' in col:
        pivot=col.index('#')
        left=col[:pivot]
        right=col[pivot:]
        
        count_X=left.count('X')
        count_Dot=len(left)-count_X
        
        new_left='.'*count_Dot+'X'*count_X
        col_matrix[i]=list(new_left)+right

row_matrix=list(map(list,zip(*col_matrix)))

for i in row_matrix:
    for j in i:
        print(j,end='')
    print()
```

## try 2
- 문제를 다시 읽어보니 유성 'X' 중에서 하나라도 '#'의 윗 row에 <br>
해당하는 칸에만 있어도 모든 유성이 멈춤을 알 수 있었다.
- 시뮬레이션 유형의 격자 이동임을 확신했다.
- 유니티 3d 게임 만들 때 ground체크 하는 거랑 비슷하다..
```python
R,S=map(int, input().split())
matrix= [list(input()) for _ in range(R)]

#유성 영역 찾기
min_row,max_row=R,-1
min_col,max_col=S,-1
for r in range(R):
    for c in range(S):
        if matrix[r][c]=='X':
            if r<min_row:
                min_row=r
            if r>max_row:
                max_row=r
            if c<min_col:
                min_col=c
            if c>max_col:
                max_col=c

#유성 부분만 별도 저장
meteor_mask=[]
for r in range(min_row,max_row+1):
    row_data=[]
    for c in range(min_col,max_col+1):
        row_data.append(matrix[r][c]=='X')
    meteor_mask.append(row_data)

#유성이 얼마나 떨어질 수 있는지 계산
max_fall=R
width=max_col-min_col+1
height=max_row-min_row+1

for c in range(width):
    meteor_bottom=-1
    for r in range(height-1,-1,-1):
        if meteor_mask[r][c]:
            meteor_bottom=r
            break
    ground_top=-1
    for r in range(height,R-min_row):
        if matrix[min_row+r][min_col+c]=='#':
            ground_top=r
            break
    if meteor_bottom == -1 or ground_top == -1:
        continue
    dist=ground_top-meteor_bottom-1
    if dist<max_fall:
        max_fall=dist

#유성 원래 위치 '.'로 초기화
for r in range(min_row,max_row+1):
    for c in range(min_col,max_col+1):
        if matrix[r][c]=='X':
            matrix[r][c]='.'

#떨어진 위치에 유성 찍기
for r in range(height):
    for c in range(width):
        if meteor_mask[r][c]:
            matrix[min_row+r+max_fall][min_col+c]='X'

#결과 출력
for row in matrix:
    print(''.join(row))
``` 
