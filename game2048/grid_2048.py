import random 
def create_grid(n=4):
    #ajouter parametre n plus tard?
    return ([[0]*n for i in range(n)])

#iteration1
def grid_add_new_tile_at_position(game_grid,n,m):#ajoute soit 2 soit 4 dans la pos desiree
    assert n<len(game_grid)
    assert m<len(game_grid)
    game_grid[n][m]=get_value_new_tile()
    return game_grid
#iteration2
def get_all_tiles(game_grid):#unifie la liste de listes en une liste globale et transforme ' ' en 0
    empt=[]
    for liste in game_grid:
        for k in liste:
            if k==0:
                empt.append(0)
            else:
                empt.append(k)
    return empt

def get_value_new_tile():#renvoie 2 ou 4 avec une proba respective de 90 et 10
    a=random.randrange(0,100)
    if a<10:
        return 4
    else:
        return 2
    
#iteration3

def get_empty_tiles_positions(liste):#renvoie la liste des positions nulles ou apostrophées
    empt=[]
    n=len(liste)
    for i in range(n):
        for j in range(n):
            if liste[i][j]==0 or liste[i][j]==' ':
                empt.append((i,j))
    return empt

def grid_get_value(grid,x,y):#basically grid[x][y]
    return grid[x][y]

def get_new_position(grid):#renvoie la position random dun 0 ou dune apostrophe
    L=get_empty_tiles_positions(grid)
    n=len(L)
    a=random.randrange(0,n)
    x=L[a]
    if grid_get_value(grid,x[0],x[1])==' ':
        grid[x[0]][x[1]]=0
    return x

def grid_add_new_tile(game_grid):#ajouter randomly un 2 ou 4 dans une case 0 ou apostrophe
    x=get_new_position(game_grid)
    grid_add_new_tile_at_position(game_grid,x[0],x[1])
    return game_grid
    
#iteration4
def init_game(n=4):
    grid=create_grid(n)
    grid_add_new_tile(grid)
    grid_add_new_tile(grid)
    return grid


    
    
    