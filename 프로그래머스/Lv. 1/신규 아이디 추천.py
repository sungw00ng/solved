def solution(new_id):
    answer = ''
    temp=''
    #1단계: 대문자는 소문자로 치환
    new_id=new_id.lower()
    
    #2단계: 소문자97~122, 숫자48~57, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    for char in new_id:
        if (97 <= ord(char) <= 122 or 48 <= ord(char) <= 57 or char in "-._"):  
            temp += char  
    new_id=temp
    
    #3단계
    while ".." in new_id:
        new_id=new_id.replace("..",".") 
    
    #4단계
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]  
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    
    #5단계
    if new_id=="":
        new_id="a"
    
    #6단계
    if len(new_id)>=16:
        new_id=new_id[:15]
        if(new_id[14]=='.'):
            new_id=new_id[:14]
        
    #7단계
    while len(new_id) < 3:
        new_id+=new_id[-1]
        
    answer=new_id
    return answer
