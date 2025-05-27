#S4_1244
#남학생 배수 toggle
'''
여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를
#중심으로 좌우가 대칭이면서 
#가장 많은 스위치를 포함하는 구간을 찾아서, 
#그 구간에 속한 스위치의 상태를 모두 바꾼다. 
#이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
'''
#남학생 1 여학생 2
N=int(input())
switch=list(map(int,input().split()))
students=int(input())

def toggle(n):
    if n==1:
        return 0
    else:
        return 1
        
for i in range(students):
    #student[0]:성별 / student[1]:받은 스위치
    student=list(map(int,input().split()))
    
    #남학생인 경우
    if student[0]==1:
        for i in range(len(switch)):
            if ((i+1)%(student[1])==0):
                switch[i]=toggle(switch[i])
                
    #여학생인 경우
    if student[0] == 2:
        center = student[1]-1 
        left = center
        right = center

        # 좌우 대칭인 최대 범위 탐색
        while left > 0 and right<N-1 and switch[left-1] == switch[right+1]:
            left -= 1
            right += 1

        # 대칭 범위의 스위치 toggle
        for k in range(left,right+1):
            switch[k] = toggle(switch[k])

#한 줄에 20개씩
for i in range(N):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
