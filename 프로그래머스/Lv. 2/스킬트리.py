def solution(skill, skill_trees):
    answer = []
    for k in skill_trees:
        str1 = ""
        for h in k:
            if h in skill:
                str1 += h
            else:
                continue
        answer.append(str1)
    cnt = 0
    for j in answer:
        if skill[:len(j)] == j:
            cnt += 1
        else:
            continue
    return cnt
