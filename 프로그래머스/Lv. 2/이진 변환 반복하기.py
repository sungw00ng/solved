def solution(s):
    cnt=0
    cnt_bin=0
    while s!="1":
        cnt+=s.count('0')
        s=s.replace('0','')
        s=bin(len(s))[2:]
        cnt_bin+=1
    return [cnt_bin,cnt]
