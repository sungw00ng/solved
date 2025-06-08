def solution(mats, park):
    R,C=len(park),len(park[0])
    
    #큰 돗자리부터 탐색
    mats.sort(reverse=True)  
    for size in mats:
        #돗자리 시작 위치(행)  
        for r in range(R-size+1):
            #돗자리 시작 위치(열)
            for c in range(C-size+1):
                flag = True 
                #시작 위치 ~ 끝 위치(행)
                for i in range(r,r+size):
                    #시작 위치 ~ 끝 위치(열)
                    for j in range(c,c+size):
                        if park[i][j] != '-1': #사람 있어서 패스
                            flag=False 
                            break
                    if not flag: #사람 있어서 패스
                        break 
                if flag:
                    return size  

    return -1  
