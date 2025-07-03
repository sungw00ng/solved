def solution(id_list, report, k):
    result=[]
    dic={}
    userID={}

    for i in id_list:
        dic[i]=set()  #id_list,value set
        userID[i]=0  #id_list,report_cnt
        
    for i in report:
        temp = i.split(' ') #[신고한 사람, 신고당한 사람]
        dic[temp[0]].add(temp[1])  #set으로 동일유저 신고 누적X
    
    for i in dic:
        for reported in dic[i]: 
            userID[reported]+=1  #신고당한사람+=1
    
    #k번 이상 신고당한 사람은 신고한 사람에게 점수 부여
    for i in dic:
        for reported in dic[i]:
            if userID[reported]>=k: 
                result.append(i)  
    print(result)
    #각 사람별로 신고당한 사람 수를 계산하여 결과를 리턴
    final_result=[result.count(user) for user in id_list]
    return final_result
