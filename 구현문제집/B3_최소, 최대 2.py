N=int(input())
for _ in range(N):
    T=int(input())
    arr=map(int,input().split())
    arr=sorted(arr)
    print(arr[0],arr[-1])
