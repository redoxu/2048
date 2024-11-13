def no_consective(liste):    #si il n'y a pas deux même nbr consicutifs
    n =len(liste)
    for j in range(n-1):
        if liste[j] == liste[j+1]:
            return False
    return True
def listesz(ligne):
    lignesanszero=[]
    for ele in ligne:
        if ele != 0:
            lignesanszero +=[ele]
    return lignesanszero

def move_row_left(ligne):
    n = len(ligne)
    L=[]
    lignesanszero=listesz(ligne)
    if no_consective(lignesanszero):
        while len(lignesanszero)<n:
            lignesanszero += [0]
    for i in range(len(lignesanszero)-1):
        if lignesanszero[i]==lignesanszero[i+1]:
            lignesanszero[i]=lignesanszero[i]*2
            lignesanszero[i+1]= 0
    lignesanszero=listesz(lignesanszero)
    while len(lignesanszero)<n:
            lignesanszero += [0]
    return lignesanszero


def move_row_right(row):
    L=row[::-1]
    l=move_row_left(L)
    return l[::-1]


def transpose(liste_de_listes):
    return [[liste_de_listes[j][i] for j in range(len(liste_de_listes))] for i in range(len(liste_de_listes[0]))]

def move_grid_left(grid):
    n = len(grid)
    grid1=grid
    for i in range(n):
        grid1[i]=move_row_left(grid[i])
    return grid1

def move_grid_right(grid):
    n = len(grid)
    grid1=grid
    for i in range(n):
        grid1[i]=move_row_right(grid[i])
    return grid1

def move_grid_up(grid):
    grid2 =grid
    n = len(grid)
    grid1=transpose(grid)
    for i in range(n):
        grid2[i]=move_row_left(grid1[i])
    return transpose(grid2)

def move_grid_down(grid):
    grid2 =grid
    n = len(grid)
    grid1=transpose(grid)
    for i in range(n):
        grid2[i]=move_row_right(grid1[i])
    return transpose(grid2)
'''
def move_grid_down(grid):
    l=grid[::-1]
    L=move_grid_up(grid)
    return L[::-1]
'''
def move_grid(grid,d):
    if d=="left":
        return move_grid_left(grid)
    elif d =="right":
        return move_grid_right(grid)
    elif d == "up":
        return move_grid_up(grid)
    elif d == "down":
        return move_grid_down(grid)
    