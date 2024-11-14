import fonctionnalite6
import argparse

def read_player_command():
    move = input("Entrez votre commande (left (left), right (right), up (up), down (down)):")
    while move not in ['left', 'right', 'up', 'down']:
        print("choix non valide")
        move = input("Entrez votre commande (left (left), right (right), up (up), down (down)):")
    return move
    
def read_size_grid():
    size = int(input("choisissez une taille inférieur ou égale à 8:  "))
    while size > 8:
        size = int(input("choisissez une taille inférieur ou égale à 8:  "))
    return size
        
def read_theme_grid():
    theme = input("choisissez un theme inferieur ou égale à 2:  ")
    while int(theme) > 2:
        theme = input("choisissez un theme inférieur ou égale à 2:  ")
    return theme

def parse_arguments():
    parser = argparse.ArgumentParser(description="Jeu 2048")
    parser.add_argument('--size', type=int, default=4, help="Taille de la grille (ex: 4 pour une grille 4x4)")
    parser.add_argument('--theme', type=str, default='Default', help="Thème du jeu (ex: Default, Chemistry, Alphabet)")
    parser.add_argument('--auto', action='store_true', help="Lancer une partie avec l'ordinateur jouant de manière aléatoire")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.auto:
        random_play()
    else:
        fonctionnalite6.game_play()
        exit(1)  
