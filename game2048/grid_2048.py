import random 
def create_grid(n=4):
    #ajouter parametre n plus tard?
    return ([[' ']*n for i in range(n)])

#iteration1
def grid_add_new_tile_at_position(game_grid,n,m):
    #ajouter peut etre une assert que n,m inferieure a la taille de la game_grid
    game_grid[n][m]=2
    return game_grid
#iteration2
def get_all_tiles(game_grid):
    empt=[]
    for liste in game_grid:
        for k in liste:
            if k==' ':
                empt.append(0)
            else:
                empt.append(k)
    return empt

def get_value_new_tile():
    a=random.randrange(0,100)
    if a<10:
        return 4
    else:
        return 2
    
