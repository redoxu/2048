import fonctionnalite6

def read_player_command():
    move = input("Entrez votre commande (left (gauche), right (droite), up (haut), down (bas)):")
    while move not in ['left', 'right', 'up', 'down']:
        print("choix non valide")
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move
    
def read_size_grid():
    size = int(input("choisissez une taille inférieur ou égale à 8:  "))
    while size > 8:
        size = int(input("choisissez une taille inférieur ou égale à 8:  "))
    return size
        
def read_theme_grid():
    theme = int(input("choisissez un theme inferieur ou égale à 2:  "))
    while theme > 2:
        theme = int(input("choisissez un theme inférieur ou égale à 2:  "))
    return str(theme)

if __name__ == '__main__':
    fonctionnalite6.game_play()
    exit(1)  
