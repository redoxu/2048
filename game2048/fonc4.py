def move_row_left(ligne):
    n = len(ligne)
    if ligne == [0]*n:
        return ligne
    while ligne[0] ==0:
        for i in range(n-1):
            ligne [i]=ligne[i+1]
        ligne[n-1]=0
    return ligne
def move_grid(grid,d):
    return 0