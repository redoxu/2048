import grid_2048 as fonctio1
import fonctionnalite5 as fonctio5
import fonc4 as fonctio4
import foctionalite2 as fonctio2
import textual_2048 as fonctio3
import random

def random_play():
    grid=fonctio1.init_game()
    fonctio2.grid_to_string_with_size_and_theme(grid)
    while not fonctio5.is_game_over(grid):
        a=random.randrange(0,4)
        list=["right","left","up","down"]
        move=list[a]
        grid=fonctio4.move_grid(grid,move)
        fonctio1.grid_add_new_tile(grid)
        fonctio2.grid_to_string_with_size_and_theme(grid)
    if fonctio5.jeu_gagnant(grid):
        return ("jeu gagnant")
    else:
        return ("jeu perdant")
        
def ask_and_read_grid_size():
    return fonctio3.read_size_grid()
def ask_and_read_grid_theme():
    return fonctio3.read_theme_grid()

def game_play():
    size=ask_and_read_grid_size()
    theme=ask_and_read_grid_theme()
    grid=fonctio1.init_game(size)
    fonctio2.grid_to_string_with_size_and_theme(grid,fonctio2.THEMES[str(theme)],size)
    while not fonctio5.is_game_over(grid):
#demander a lutilisateur son move... reste à faire
        move=fonctio3.read_player_command() 
        grid=fonctio4.move_grid(grid,move)
        fonctio1.grid_add_new_tile(grid)
        fonctio2.grid_to_string_with_size_and_theme(grid,fonctio2.THEMES[str(theme)],size)
    if fonctio5.jeu_gagnant(grid):
        return ("jeu gagnant")
    else:
        return ("jeu perdant")




    