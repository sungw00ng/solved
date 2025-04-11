def solution(mats, park):
    answer = -1

    #"-1"만 1로 보고, 나머지는 0 처리
    board = [
        [1 if x == "-1" else 0 for x in row]
        for row in park
    ]
    
    rows = len(board)
    cols = len(board[0])
    dp = [[0]*cols for _ in range(rows)]

    MatSize = 0

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                #n=1
                if i == 0 or j == 0:
                    dp[i][j] = 1
                #n>=2
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                MatSize = max(MatSize, dp[i][j])
    
    #내림차순
    mats=sorted(mats,reverse=True)
    
    #결과비교
    for i in range(len(mats)):
        if(mats[i]<=MatSize):
            answer=mats[i]
            break
            
    return answer
