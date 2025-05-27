N=int(input())
for _ in range(N):
    a,b=input().split()
    hap=int(a, 2)+int(b, 2)
    print(bin(hap)[2:])
