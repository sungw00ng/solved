sound=list(input())
ans=0

if sound[0] != "q" or sound[-1] != "k" or len(sound) % 5:
    print(-1)
    exit()

def find_quack(start):
    quack="quack"
    j=0
    global ans
    new_ori=True
    for i in range(start,len(sound)):
        #일치하는지
        if sound[i]==quack[j]:
            if sound[i]=="k":
                if new_ori:
                    ans+=1
                    new_ori=False
                j=0
                sound[i]=0
                continue
            j+=1
            sound[i]=0

for i in range(len(sound)-4):
    if sound[i]=="q":
        find_quack(i)

if any(sound) or ans==0:
    print(-1)
else:
    print(ans)
