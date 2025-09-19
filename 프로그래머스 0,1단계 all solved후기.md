## 러닝 커브 점검
<img width="500" src="https://github.com/user-attachments/assets/b408d167-380b-4b43-a509-a0002f217b0d" /><br>
```text
mysql(1~5), 0단계, 1단계해서 총 65일을 사용했다.
순서는 1단계->0단계,2단계 (동시) 로 진행했다.
0단계를 풀면서 2단계를 절반 정도 풀어두었다.
사실 백준 짬바(?)로 인해 0단계와 1단계는 빨리 밀어놔야되는 단계였어서
한달 정도면 끝날줄 알았는데
노력 대비 성과가 절반 정도였던 것 같아서 아쉽다.
그만큼 기초가 부족했음을 인정하고 탄탄해지는 65일이라고 회고한다..
이제 5단계 마지막까지는 총 179문제가 남았는데
이상적으로 하루 4~5문제 정도면 올해 안에는 모두 마무리지을 수 있으니
마음 단단히 먹고 열심히 하자.
```

## 프로그래머스 0단계 all solve
<img width="600" src="https://github.com/user-attachments/assets/ff3d218e-fd9e-4395-bf96-35a5bef6bdce" /> <br>

### 후기
```text
1단계보다 더 오랜 시간이 걸린 0단계다...
솔직히 1단계보다 어려운 문제들도 많았다고 생각한다.
기초는 탄탄하게 쌓을 수 있는데 1단계 대비 문제량이 2.5배이므로
그냥 이건 .. 오래 앉아서 빨리 그리고 많이 익히고
탈출하는게 정답이라고밖에... 표현을 못하겠다.
```


<br>

## 프로그래머스 1단계 all solve 
<br><img width="600" alt="올솔브" src="https://github.com/user-attachments/assets/a963d123-cad0-4477-a2ee-6a990c1e7062" /><br>
## 서론
어떤 벽에 좀 부딪히다보니 기초를 다듬고 싶었다. <br>
DP나 그래프 문제를 더 푸는 방법도 물론 좋지만, <br>
기초적인 자료구조 공부를 할 시간이 더 필요하다고 느꼈다. <br>
이에 있어서, 프로그래머스 1단계는 좋은 문제집이라고 생각했다. <br>

처음에는 정답률이 높은 문제 순으로 해결하다 보니 금방 모두 풀 수 있을 것이라 생각했는데.. <br>
20문제 쯤 남으니까 긴장감을 느낄 수 있는 문제가 몇몇 존재했다. <br>

1단계의 어려운 문제를 도전하시는 분들을 위해, <br>
그리고 스스로 다시 복습할 때를 위해서,<br>
적용이 빠른 기본 테크닉 일부를 남겨보려고 한다. <br>

<br><br>

## 본론
### if i in dic: 딕셔너리 기본기, 빈도율 매우 높음 <br>
```python
dic={}
if i in dic:
  dic[i]+=1
else:
  dic[i]=1
```
<br><br>

### 자주 쓰는 enumerate, items(), 빈도율 높음
- for key,value in dict.items()
- for idx,value in enumerate(iterable):

<br><br>

### 아스키 코드 변환하기, 빈도율 높음
- ord, chr

<br><br>

### 에라토스테네스의 체, 빈도율 높음
```python
#약수 구하기
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                count+=1
```
- 그런데 범위 안에 있는 약수의 개수를 모두 구하려면?(순서쌍 원리)
```python
                if j<i//j:
                    count+=1
```
>[Lv1_기사단원의 무기](https://school.programmers.co.kr/learn/courses/30/lessons/136798)<br>

<br><br>
### immutable한 것과 mutable한 것 <br>

| 유형        | 예시 객체             | 변경 가능 여부  |
|-------------|------------------------|------------------|
| Immutable   | `int`, `float`, `str`, `tuple` | ❌ 변경 불가 |
| Mutable     | `list`, `dict`         | ✅ 변경 가능     |

- 문자열에서 split()함수를 사용하면 자동으로 list가 되니 주의
<br><br>
### list의 remove와 문자열의 replace (혼동 주의)

| 항목           | 리스트 `remove()`           | 문자열 `replace()`   |
| ------------ | ------------------------ | ----------------- |
| **동작 대상**    | 리스트 (`list`)             | 문자열 (`str`)       |
| **제거/변경 횟수** | **처음 나오는 1개만 제거**        | **모든 대상 치환 (기본)** |
| **예외 발생**    | 요소 없으면 `ValueError`      | 대상 없으면 아무 일 없음    |
| **변경 방식**    | 리스트 **자체 수정 (in-place)** | **새 문자열 반환**      |

>[Lv1_옹알이 (2)](https://school.programmers.co.kr/learn/courses/30/lessons/42889)<br>

<br><br>

### reverse 뒤집기 대신
- list[::-1]도 가능하다. <br>
[Lv1_택배 상자 꺼내기](https://school.programmers.co.kr/learn/courses/30/lessons/389478)<br>

<br><br>

### 순열과 조합
```python
from itertools import permutations, combinations, product, combinations_with_replacement

data = [1, 2, 3]
print(list(permutations(data, 2)))                   # 순열 (order matters)
print(list(combinations(data, 2)))                   # 조합 (order doesn't matter)
print(list(product([1, 2], repeat=2)))               # 중복 순열 (cartesian product)
print(list(combinations_with_replacement([1, 2], 2)))# 중복 조합

#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
#[(1, 2), (1, 3), (2, 3)]
#[(1, 1), (1, 2), (2, 1), (2, 2)]
#[(1, 1), (1, 2), (2, 2)]

```
>[Lv1_삼총사](https://school.programmers.co.kr/learn/courses/30/lessons/131705)<br>
>[Lv1_소수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12977)<br>
<br><br>

### zip,all,any,chain
```python
from itertools import chain

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

# zip 사용
for a, b in zip(lst1, lst2):
    print((a, b))  # (1,4), (2,5), (3,6)

# all: 모든 요소가 3보다 작니?
print(all(x < 3 for x in lst1))  # False

# any: 하나라도 5보다 큰 값 있니?
print(any(x > 5 for x in lst2))  # True

# chain: 리스트 이어붙이기
print(list(chain(lst1, lst2)))   # [1, 2, 3, 4, 5, 6]
```
>[Lv1_음양 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/76501https://school.programmers.co.kr/learn/courses/30/lessons/76501)<br>


<br><br>

### 람다 함수
```python
data = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
data.sort(key=lambda x: x[0])
print(data)
# [(1, 'banana'), (2, 'cherry'), (3, 'apple')]
```
- 정렬 한 번에 dic value의 내림차순, 같으면 오름차순을 한다면?
```python
  return sorted(result, key=lambda x: (-result[x], x))
```
>[Lv1_실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889)<br>

 <br><br>
 
### for문에서 flag를 유도하는 함정 문제
>[Lv1_문자열 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/140108)<br>

<br><br>

### deque를 쓰지 않아도 stack에서 pop(0)으로 첫 번째 원소를 지울 수 있다.

<br><br>

### 진법 변환
| 진법   | 함수          | 예시 입력            | 반환값        | 설명                              |
| ---- | ----------- | ---------------- | ---------- | ------------------------------- |
| 2진수  | `bin(x)`    | `bin(10)`        | `'0b1010'` | 정수 `10`을 2진수 문자열로 변환            |
| 8진수  | `oct(x)`    | `oct(10)`        | `'0o12'`   | 정수 `10`을 8진수 문자열로 변환            |
| 16진수 | `hex(x)`    | `hex(10)`        | `'0xa'`    | 정수 `10`을 16진수 문자열로 변환           |
| 10진수 | `int(s, b)` | `int("1010", 2)` | `10`       | 문자열 `"1010"`을 2진수로 해석해 10진수로 변환 |

<br><br>

### 리스트 내포, 딕셔너리(k:문자열, v:리스트 or 숫자) 내포
```python
final_result=[result.count(user) for user in id_list]
giftscore = {f: 0 for f in friends}
ab_history = {f: [] for f in friends}
```
>[신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334)<br>
>[가장 많이 받은 선물](https://school.programmers.co.kr/learn/courses/30/lessons/258712)<br>



