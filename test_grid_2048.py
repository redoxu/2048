from game2048.grid_2048 import *
from pytest import *


def test_create_grid(n=4):
    assert create_grid(n) == [[' ']*n for i in range(n)]
#iteration1
def test_grid_add_new_tile_at_position():
    game_grid=create_grid(4)
    game_grid=grid_add_new_tile_at_position(game_grid,1,1)
    assert game_grid==[[' ',' ',' ', ' '],[' ', 2 ,' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]
    
#iteration2
def test_grid_add_new_tile_at_position():
    game_grid=create_grid(4)
    game_grid=grid_add_new_tile_at_position(game_grid,1,1)
    tiles = get_all_tiles(game_grid)
    assert 2 in tiles or 4 in tiles

def test_get_value_new_tile():
    assert get_value_new_tile() in {2, 4}


def test_get_all_tiles():
    assert get_all_tiles( [[' ',4,8,2], [' ',' ',' ',' '], [' ',512,32,64], [1024,2048,512, ' ']]) == [0,4,8,2,0,0,0,0,0,512,32,64, 1024,2048,512,0]
    assert get_all_tiles([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]]) == [16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]
    assert get_all_tiles(create_grid(3))== [0 for i in range(9)]
