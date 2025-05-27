def star_19(n):
    if n==1:
        print('*')
        return
    
    width=4*n-3
    matrix=[[' ']*width for _ in range(width)]
    
    #recursion draw
    def draw(n,offset):
        if n==1:
            matrix[offset][offset]='*'
            return
        
        length=4*n-3
        
        for i in range(length):
            #위
            matrix[offset][offset+i]='*'
            #아래
            matrix[offset+length-1][offset+i]='*'
            #왼
            matrix[offset+i][offset]='*'
            #오
            matrix[offset+i][offset+length-1]='*'
            
        draw(n-1,offset+2)
    draw(n,0)
    for row in matrix:
        print(''.join(row))
N=int(input())
star_19(N)
