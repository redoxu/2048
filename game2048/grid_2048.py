from random import random, choice, randint
def create_grid(n):
    game_grid = [[' ' for i in range(n)] for j in range(n)]
    return game_grid

def grid_add_new_tile_at_position(game_grid,i,j):
    game_grid[i][j] = 2
    return game_grid

def get_all_tiles(grid):
    tiles = []
    for ligne in grid :
        for tile in ligne:
            if tile == ' ' :
                tiles.append(0)
            else:
                tiles.append(tile)
    return tiles

def get_value_new_tile():
    a = random()
    if a < 0.9:
        return 2
    return 4

def get_empty_tiles_positions(grid):
    empty_tiles_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in [0, ' ']:
                empty_tiles_positions.append((i,j))
    return empty_tiles_positions

def grid_get_value(grid,x,y):
    if grid[x][y] == ' ':
        return 0
    return grid[x][y]

def get_new_position(grid):
    return choice(get_empty_tiles_positions(grid))

def grid_add_new_tile(grid):
    position = get_new_position(grid)
    grid[position[0]][position[1]] = get_value_new_tile()
    return grid

def init_game(n):
    grid = create_grid(n)
    grid_add_new_tile(grid)
    grid_add_new_tile(grid)
    return grid