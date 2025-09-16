## A번 할인이 필요해
https://www.acmicpc.net/problem/34323 <br>

```text
n%할인과 M+1 중 뭐가 더 나은지 고르는 문제였다. (최솟값으로)
n%할인은 그냥 나눠서 100곱하고,
M+1이 문제였는데 곰곰히 생각해보니
물건을 구매했을 때 N%할인을 (물건개수-1)로 낮추는 것이
핵심이었다.
M+1을 그냥 M으로 두면 쉽게 풀리는 문제였다. 
```

```python3
import sys
input=sys.stdin.readline
N,M,S=map(int,input().split())
nprice=(M+1)*S*(100-N)//100
mprice=M*S
print(min(nprice,mprice))
```
