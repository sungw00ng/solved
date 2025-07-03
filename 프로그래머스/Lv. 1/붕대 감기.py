def solution(bandage, health, attacks):
    #bandage => [시전 시간,초당 회복량,추가 회복량]
    #attacks => [공격 시간,피해량]

    last_time=attacks[-1][0] #마지막 공격 시간
    max_health=health #최대 체력
    attack_idx=0 #공격 순서
    bandage_cnt=0 # 붕대 감기 연속 시간 카운트

    for second in range(1,last_time+1):
        #현재 시간이 공격 발생 시간인지 확인
        if second==attacks[attack_idx][0]:
            #공격이 발생한 시간이라면
            health-=attacks[attack_idx][1]
            attack_idx+=1 #다음 공격으로 이동
            
            #시간 초기화
            bandage_cnt=0
            
            #체력 0 이하
            if health<=0:
                return -1
            
            #붕대 못함
            continue

        #붕대 감기
        health+=bandage[1] 
        bandage_cnt+=1
        # 최대 체력 제한
        if health>max_health:
            health=max_health
        
        # 붕대 감기 성공
        if bandage_cnt==bandage[0]:
            health+=bandage[2] 
            bandage_cnt=0
            
            # 최대 체력 제한
            if health>max_health:
                health=max_health
                
    return health
