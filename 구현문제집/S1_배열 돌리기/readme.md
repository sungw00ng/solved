## 문제 이해
<img src="https://github.com/user-attachments/assets/85de65b0-4b91-4ddb-b243-a10785d07d89" width="700"/><br>
- 주 대각선은 (1,1)...(n,n) 대각선
- 부 대각선은 (n,1)...(1,n) 대각선
- 문제에서 제시한 형식 외에 모서리 부분은 고정인 듯하다.
## 코드
```python
T=int(input())
for _ in range(T):
    N,degree=map(int,input().split())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    degree=(degree+360)%360  #음수 각도 처리

    if degree==0:
        for row in matrix:
            print(*row)
        continue

    for _ in range(degree//45):
        mid=N//2
        new_matrix=[row[:] for row in matrix]  

        for i in range(N):
            #1
            new_matrix[i][mid]=matrix[i][i]     
            #2
            new_matrix[i][N-1-i]=matrix[i][mid]    
            #3
            new_matrix[mid][N-1-i]=matrix[i][N-1-i] 
            #4
            new_matrix[i][i]=matrix[mid][i]             
        matrix=new_matrix

    for row in matrix:
        print(*row)
```
