N=int(input())
cnt=0
for _ in range(N):
    group_check=True
    word=input()
    if(len(word)>=3):
        for i in range(2,len(word)):
            if(word[i] != word[i-1] and word[i] in word[:i-1]):
                group_check=False
    if group_check:
        cnt+=1
        
print(cnt)
