def solution(survey, choices):
    dict={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    #점수 더하기
    for i in range(len(choices)):
        str1=survey[i][0]
        str2=survey[i][1]
        if choices[i]==1:
            dict[str1]+=3
        elif choices[i]==2:
            dict[str1]+=2
        elif choices[i]==3:
            dict[str1]+=1
        elif choices[i]==5:
            dict[str2]+=1
        elif choices[i]==6:
            dict[str2]+=2
        elif choices[i]==7:
            dict[str2]+=3
    #result
    answer=[]
    answer.append('R' if dict['R']>=dict['T'] else 'T')
    answer.append('C' if dict['C']>=dict['F'] else 'F')
    answer.append('J' if dict['J']>=dict['M'] else 'M')
    answer.append('A' if dict['A']>=dict['N'] else 'N')
    
    return ''.join(answer)
