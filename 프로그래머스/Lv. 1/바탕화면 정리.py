def solution(wallpaper):
    result=[]
    first_row,first_col=0,0
    end_row,end_col=0,0
    Min,Max=52,-1
    for i,v in enumerate(wallpaper):
        if '#' in v:
            first_row=i
            break
    for i in wallpaper:
        for idx,col in enumerate(i):
            if col=='#' and idx<Min:
                Min=idx
                break
        first_col=Min
        
    for i,v in enumerate(wallpaper):
        if '#' in v:
            end_row=i+1
    
    for i in wallpaper:
        for idx,col in enumerate(i):
            if col=='#' and idx>Max:
                Max=idx
    end_col=Max+1
    result.append(first_row)
    result.append(first_col)
    result.append(end_row)
    result.append(end_col)
    return result
