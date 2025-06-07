n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]
board = [[0]*n for _ in range(n)]

#dict{학생번호[0] : 좋아하는 학생들}
likes = {s[0]: s[1:] for s in students}

#방향: 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for student in students:
    num=student[0]
    fav=student[1:]
    candidates=[]

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue  # 이미 앉은 자리

            like_cnt=0
            empty_cnt=0

            for d in range(4):
                ni=i+dx[d]
                nj=j+dy[d]
                #index error fix
                if 0<=ni<n and 0<=nj<n:
                    if board[ni][nj] in fav:
                        like_cnt+=1
                    elif board[ni][nj]==0:
                        empty_cnt+=1
            
            # 정렬 기준: 좋아하는 학생 수 desc, 빈 칸 수 desc, 행 번호 Asc, 열 번호 Asc
            candidates.append((-like_cnt,-empty_cnt,i,j ))  
    
    candidates.sort()
    x,y=candidates[0][2],candidates[0][3]
    board[x][y]=num

score_table=[0,1,10,100,1000]
answer=0

for i in range(n):
    for j in range(n):
        student=board[i][j]
        fav=likes[student]
        cnt=0
        for d in range(4):
            ni=i+dx[d]
            nj=j+dy[d]
            if 0<=ni<n and 0<=nj<n:
                if board[ni][nj] in fav:
                    cnt+=1
        answer+=score_table[cnt]
print(answer)
