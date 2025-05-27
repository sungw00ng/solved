#소의 번호가 1이상 10이하
N=int(input())
dic={}
cnt=0
for _ in range(N):
    a,b=map(int,input().split())
    if a not in dic:
        dic[a]=b
    elif dic[a] != b:
        dic[a]=b
        cnt+=1

print(cnt)
