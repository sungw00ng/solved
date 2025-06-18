def solution(n, lost, reserve):
    x_reserve=[r for r in reserve if r not in lost]
    x_lost=[l for l in lost if l not in reserve]
    for i in sorted(x_reserve):
        a=i+1
        b=i-1
        if b in x_lost:
            x_lost.remove(b)
        elif a in x_lost:
            x_lost.remove(a)
        
    return n-len(x_lost)
