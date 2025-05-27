N=int(input())
s=input()

count=0
for i in range(N-1):
    if s[i]=='E' and s[i+1]=='W':
        count+=1

print(count)
