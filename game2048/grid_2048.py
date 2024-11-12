import random
def create_grid(n=4):
    game_grid = []
    for i in range(n):
        game_grid.append(n*[' '])
    return game_grid

def grid_add_new_tile_at_position(game_grid,i,j):
    game_grid[i][j] = get_value_new_tile()
    return game_grid

def get_all_tiles(game_grid):
    L = []
    for i in range(len(game_grid[0])):
        for j in range(len(game_grid[0])):
            if game_grid[i][j]==' ':
                L.append(0)
            else:
                L.append(game_grid[i][j])
    return L

def get_value_new_tile():
    n = random.randint(1,100)
    if n>= 10:
        return 2
    else :
        return 4

def get_empty_tiles_positions(game_grid):
    L = []
    for i in range(len(game_grid[0])):
        for j in range(len(game_grid[0])):
            if game_grid[i][j] in {0,' '}:
                L.append((i, j))
    return L 

def get_new_position(grid):
    L = get_empty_tiles_positions(grid)
    return L[random.randint(0,len(L)-1)]
    
def grid_get_value(grid,x,y):
    if grid[x][y] == ' ':
        return 0
    return grid[x][y]
    
def grid_add_new_tile(game_grid):
   L = game_grid
   L[get_new_position(game_grid)[0]][get_new_position(game_grid)[1]]=get_value_new_tile()
   return L 
    
def init_game(n=4):
    grid = create_grid(n)
    grid_add_new_tile(grid)
    grid_add_new_tile(grid)
    return grid
    
    