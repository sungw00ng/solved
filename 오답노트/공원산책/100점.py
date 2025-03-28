def solution(park, routes):
    #시작점 찾기
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = i, j
                break
    
    #경로
    for route in routes:
        direction, distance = route.split() #direction="E", distance="2"
        distance = int(distance) 
        
        #지속적인 값 변화
        new_x, new_y = x, y
        
        for _ in range(distance):
            if direction == "E":
                new_y += 1
            elif direction == "W":
                new_y -= 1
            elif direction == "N":
                new_x -= 1
            elif direction == "S":
                new_x += 1

            # 공원 범위 안에 있는가 or 장애물이 있는가
            if not (0 <= new_x < len(park) and 0 <= new_y < len(park[0])) or \
            park[new_x][new_y] == "X":
                break
        else:
            x, y = new_x, new_y

    return [x, y]
