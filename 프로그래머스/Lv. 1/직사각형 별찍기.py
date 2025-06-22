a, b = map(int, input().strip().split(' '))
matrix=[['*' for _ in range(a)] for _ in range(b)]
for i in matrix:
    for j in i:
        print(j,end='')
    print()
