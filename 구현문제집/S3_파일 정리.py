N=int(input())
end={}

#확장자 저장
for _ in range(N):
    word=input().split('.')
    word_key=word[1]
    if word_key in end:
        end[word_key]+=1
    else:
        end[word_key]=1

for i in sorted(end):
    print(i,end[i])
