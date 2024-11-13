def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move not in ['g', 'd', 'h', 'b']:
        print("choix non valide")
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move
    
def read_size_grid():
    size = int(input("choisissez une taille inférieur ou égale à 8:  "))
    while size > 8:
        size = int(input("choisissez une taille inférieur ou égale à 8:  "))
    return size
        
def read_theme_grid():
    theme = int(input("choisissez une taille inférieur ou égale à 8:  "))
    while theme > 8:
        theme = int(input("choisissez une taille inférieur ou égale à 8:  "))
    return theme