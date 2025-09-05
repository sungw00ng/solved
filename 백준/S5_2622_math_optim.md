## 브루트포스
```python3
n=int(input())
cnt=0
for i in range(n+1): #low
    for j in range(i,n+1): #middle
        k=n-i-j
        if k>=i+j:
            continue
        else:
            #k>=j
            if j>k:
                break
            cnt+=1
print(cnt)
```

# 비트 마스킹
```python3
n=int(input()) 
print((n*n+6)//12-n//4*(n+2>>2))
```
