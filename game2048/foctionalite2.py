import copy

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def grid_to_string(game_grid, n):
    # Convertir tous les éléments en chaînes
    for i in range(n):
        for j in range(n):
            game_grid[i][j] = str(game_grid[i][j])
    
    # Créer une ligne de séparation entre les lignes de la grille
    entrelignes = " ===" * n + "\n"
    
    # Joindre chaque ligne de la grille avec les séparateurs de colonne
    str1 = entrelignes
    for ligne in game_grid:
        str1 += "| "
        for ele in ligne :
            str1 += str(ele)+" | "
        str1 = str1[:-1]
        str1 += "\n"+ entrelignes
        
    # Retourner la grille formatée avec des lignes de séparation au début et à la fin
    return  str1[:-1]
    
def long_value(grid_game):
    m=0
    for i in range(len(grid_game)):
        for j in range(len(grid_game)):
            if len(grid_game[i][j])>=m:
                m = len(grid_game[i][j])
    return m


def grid_to_string_with_size(game_grid,n):
    m = long_value(game_grid)
    # Convertir tous les éléments en chaînes
    for i in range(n):
        for j in range(n):
            game_grid[i][j] = str(game_grid[i][j])
    
    # Créer une ligne de séparation entre les lignes de la grille
    egales = ' '+("=")
    entrelignes = " ===" * n + "\n"
    
    # Joindre chaque ligne de la grille avec les séparateurs de colonne
    str1 = entrelignes
    for ligne in game_grid:
        str1 += "| "
        for ele in ligne :
            str1 += str(ele)+" | "
        str1 = str1[:-1]
        str1 += "\n"+ entrelignes
        
    # Retourner la grille formatée avec des lignes de séparation au début et à la fin
    return  str1[:-1]


def long_value_with_theme(grid_game,theme):
    m=0
    for i in range(len(grid_game)):
        for j in range(len(grid_game)):
            if len(theme[int(grid_game[i][j])])>m:
                m = len(theme[int(grid_game[i][j])])
    return m

def grid_to_string_with_size_and_theme(game_grid,theme=THEMES["0"],n=4):
    m = long_value_with_theme(game_grid,theme)
    game_grid_str = copy.deepcopy(game_grid)
    # Convertir tous les éléments en chaînes
    for i in range(n):
        for j in range(n):
            game_grid_str[i][j] = str(game_grid_str[i][j])
    
    # Créer une ligne de séparation entre les lignes de la grille
    egales = ' '+("="*m)
    entrelignes = egales * n + "\n"
    
    # Joindre chaque ligne de la grille avec les séparateurs de colonne
    str1 = entrelignes
    for ligne in game_grid_str:
        str1 += "|"
        for ele in ligne :
            wa3 =theme[int(ele)]
            while len(wa3)<m:
                wa3 +=' '
                
            str1 += wa3+"|"
        str1 = str1
        str1 += "\n"+ entrelignes
        
    # Retourner la grille formatée avec des lignes de séparation au début et à la fin
    return  str1[:-1]

"""
def grid_to_grid_str(game_grid):
    n = len(game_grid)
    game_grid_str = [[0]*n for i in range(n)]
    # Convertir tous les éléments en chaînes
    for i in range(n):
        for j in range(n):
            game_grid_str[i][j] = game_grid[i][j]
            game_grid_str[i][j] = str(game_grid_str[i][j])
    return game_grid_str
"""