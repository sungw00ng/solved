def solution(s):
    s=s.split(' ')
    result=[]
    for word in s: 
        if word:
            result.append(word[0].upper()+word[1:].lower())
        else:
            result.append('')
            
    return ' '.join(result)
