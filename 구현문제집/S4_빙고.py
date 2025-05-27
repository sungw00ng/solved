import sys
input=sys.stdin.readline
Bingo=[]
Attack=[]
cnt=0

#빙고판
for _ in range(5):
    Bingo.append(list(map(int, input().split())))
#Attack
for _ in range(5):
    Attack.extend(list(map(int, input().split())))
# 숫자를 지우는 함수
def mark(num):
    for i in range(5):
        for j in range(5):
            if Bingo[i][j]==num:
                Bingo[i][j]=0
# 빙고 개수를 세는 함수
def check_bingo():
    bingo=0
    #가로 
    for i in range(5):
        if all(Bingo[i][j]==0 for j in range(5)):
            bingo+=1
    #세로 
    for j in range(5):
        if all(Bingo[i][j]==0 for i in range(5)):
            bingo+=1
    #대각선 
    if all(Bingo[i][i]==0 for i in range(5)):
        bingo+=1
    if all(Bingo[i][4-i]==0 for i in range(5)):
        bingo+=1
    return bingo

#결과
for num in Attack:
    cnt += 1
    mark(num)
    if check_bingo() >= 3:
        print(cnt)
        break
