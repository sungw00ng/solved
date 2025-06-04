## 딕셔너리를 함수 밖으로 빼는 경우
- 전역변수를 여러 함수가 공유하면 코드가 복잡해지고 버그 찾기 어려워진다. <br>
- 함수의 독립성과 재사용성이 떨어짐 → 다른 데이터로 함수 쓰기 어려워진다. <br>
- 멀티스레드나 병렬처리 시 상태 관리가 힘들어진다. <br>
```python
levels={}
def divide(arr,level=0):
    if not arr:
        return
    mid=len(arr)//2
    if level not in levels:
        levels[level]=[]
    levels[level].append(arr[mid])

    #재귀 왼쪽 오른쪽 분할
    divide(arr[:mid],level+1)
    divide(arr[mid+1:],level+1)
```

## 딕셔너리를 함수 안에 넣는 경우 
- 독립적으로 동작하고, 상태도 명확하게 관리될 수 있다. <br>
```python
def divide(arr,level=0,levels=None):
    if not arr:
        return
    
    if levels is None:
        levels={}
        
    mid=len(arr) // 2
    
    if level not in levels:
        levels[level]=[]
        
    levels[level].append(arr[mid])
    
    #재귀 왼쪽 오른쪽 분할 
    divide(arr[:mid],level+1,levels)
    divide(arr[mid+1:],level+1,levels)
```

## 답
```python
#깊이 완전 트리 (2**k - 1)개의 노드
K=int(input())
arr=list(map(int,input().split()))

def divide(arr,level=0,levels=None):
    if not arr:
        return
    
    if levels is None:
        levels={}
        
    mid=len(arr) // 2
    
    if level not in levels:
        levels[level]=[]
        
    levels[level].append(arr[mid])
    
    #재귀 왼쪽 오른쪽 분할 
    divide(arr[:mid],level+1,levels)
    divide(arr[mid+1:],level+1,levels)
    
    #출력
    if level==0:
        for level in sorted(levels):
            print(*levels[level]) 
            
divide(arr,level=0,levels=None)
```
