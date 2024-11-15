import tkinter as tk
import grid_2048 as fonctio1
import fonctionnalite5 as fonctio5
import fonc4
import copy
from functools import partial

theme = ''
size = 4 

TILE_COLORS = {
    0: ("#cdc1b4", "#776e65"),
    2: ("#eee4da", "#776e65"),
    4: ("#ede0c8", "#776e65"),
    8: ("#f2b179", "#f9f6f2"),
    16: ("#f59563", "#f9f6f2"),
    32: ("#f67c5f", "#f9f6f2"),
    64: ("#f65e3b", "#f9f6f2"),
    128: ("#edcf72", "#f9f6f2"),
    256: ("#edcc61", "#f9f6f2"),
    512: ("#edc850", "#f9f6f2"),
    1024: ("#edc53f", "#f9f6f2"),
    2048: ("#edc22e", "#f9f6f2"),
}

def display_and_update_graphical_grid(grid_game, labels):
    """Mettre à jour les couleurs et valeurs de la grille à l'écran."""
    for i in range(len(labels)):
        for j in range(len(labels)):
            value = grid_game[i][j]
            bg_color, fg_color = TILE_COLORS.get(value, ("#cdc1b4", "#776e65"))
            
            labels[i][j].config(
                text=str(value) if value != 0 else "",
                bg=bg_color,
                fg=fg_color
            )
    
def create_game_grid(size,root):
    grid = fonctio1.init_game(size)

    background = tk.Frame(root, bg="#bbada0")
    background.grid(padx=10, pady=10, row=0, column=0)

    labels = []
    for i in range(size):
        row_labels = []
        for j in range(size):
            frame = tk.Frame(background, width=100, height=100, bg="#cdc1b4", bd=5)
            frame.grid(row=i, column=j, padx=5, pady=5)

            label = tk.Label(frame, text="", bg="#cdc1b4", fg="#776e65", font=("Helvetica", 24, "bold"), width=4, height=2)
            label.grid()
            row_labels.append(label)
        labels.append(row_labels)

    display_and_update_graphical_grid(grid, labels)
    return  (grid, labels)


def move_grid(grid, direction):
    gridd = copy.deepcopy(grid)
    grid = fonc4.move_grid(grid, direction)
    if gridd != grid:
        grid = fonctio1.grid_add_new_tile(grid)
    return grid

def check_game_state(grid, root):
    if fonctio5.jeu_gagnant(grid):
        root.quit()
    if fonctio5.is_game_over(grid):
        root.quit()
        
def game_play_gui():
    root = tk.Tk()
    root.title("Jeu 2048")
    
    setup = tk.Toplevel(root)                           # creats second window
    setup.title("configuration")
    
    label = tk.Label(setup, text="Choose grid size")
    label.pack()
    
    spinbox = tk.Spinbox(setup, from_=4, to=8)          # creats selection widget with arrows
    spinbox.pack()
    
    label = tk.Label(setup, text="Choose grid size")
    label.pack()
    
    listbox = tk.Listbox(setup, height=10, width=30, selectmode=tk.SINGLE)   # creats selection list box
    listbox.pack()
# Add items to the Listbox
    items = ["Default", "Chemistry", "Alphabet"]
    for item in items:
        listbox.insert(tk.END, item)
        
# Function to be called when an item is selected

    def on_select(theme, size, root):
    # Get the index of the selected item
        selected_index = listbox.curselection()
        selected_item = listbox.get(selected_index)
        theme = selected_item
        size = int(spinbox.get())
        setup.destroy()
        # creation of th game grid 
        grid, labels = create_game_grid(size,root)
    # function to call after arrow press
        def on_move(direction: str):            
            nonlocal grid
            nonlocal labels
            grid = move_grid(grid, direction)
            display_and_update_graphical_grid(grid, labels)
            check_game_state(grid, root)

    # control arrows definition       
        root.bind("<Left>", lambda event: on_move('left'))          
        root.bind("<Right>", lambda event: on_move('right'))
        root.bind("<Up>", lambda event: on_move('up'))
        root.bind("<Down>", lambda event: on_move('down'))

# Bind the selection event to the on_select function

    listbox.bind("<<ListboxSelect>>", lambda event: on_select(theme, size, root))
    
# creation of th game grid 
    grid, labels = create_game_grid(size,root)
# function to call after arrow press

    def on_move(direction: str):            
        nonlocal grid
        nonlocal labels
        grid = move_grid(grid, direction)
        display_and_update_graphical_grid(grid, labels)
        check_game_state(grid, root)
       
# quit button definition  
        
    button = tk.Button(setup, command=root.quit, text="quit")
    button.pack(padx=40)
    
# control arrows definition
        
    root.bind("<Left>", lambda event: on_move('left'))          
    root.bind("<Right>", lambda event: on_move('right'))
    root.bind("<Up>", lambda event: on_move('up'))
    root.bind("<Down>", lambda event: on_move('down'))

# start of game/window loop

    root.mainloop()

game_play_gui()
