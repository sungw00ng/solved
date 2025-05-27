student=[0]*31
for i in range(1,29):
    num=int(input())
    student[num]=num
for j in range(1,31):
    if student[j]==0:
        print(j)
