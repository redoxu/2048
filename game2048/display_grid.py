import tkinter as tk
import grid_2048 as fonctio1
import fonctionnalite5 as fonctio5
import fonc4
import copy
from functools import partial

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
    for i in range(4):
        for j in range(4):
            value = grid_game[i][j]
            bg_color, fg_color = TILE_COLORS.get(value, ("#cdc1b4", "#776e65"))
            
            labels[i][j].config(
                text=str(value) if value != 0 else "",
                bg=bg_color,
                fg=fg_color
            )



def game_play_gui():
    root = tk.Tk()
    root.title("Jeu 2048")

    grid = fonctio1.init_game(4)
    game_window = tk.Toplevel(root)
    game_window.title("Jeu 2048")

    background = tk.Frame(root, bg="#bbada0")
    background.grid(padx=10, pady=10, row=0, column=0)

    labels = []
    for i in range(4):
        row_labels = []
        for j in range(4):
            frame = tk.Frame(
                background,
                width=100,
                height=100,
                bg="#cdc1b4",
                bd=5
            )
            frame.grid(row=i, column=j, padx=5, pady=5)

            label = tk.Label(
                frame,
                text="",
                bg="#cdc1b4",
                fg="#776e65",
                font=("Helvetica", 24, "bold"),
                width=4,
                height=2
            )
            label.grid()
            row_labels.append(label)
        labels.append(row_labels)

    display_and_update_graphical_grid(grid, labels)

    def on_move(direction):
        nonlocal grid
        gridd = copy.deepcopy(grid)
        grid = fonc4.move_grid(grid, direction)
        if gridd == grid:
            return
        if gridd != grid:
            grid = fonctio1.grid_add_new_tile(grid)
        display_and_update_graphical_grid(grid, labels)
        if fonctio5.jeu_gagnant(grid):
            root.quit()
        if fonctio5.is_game_over(grid):
            root.quit()

    root.bind("<Left>", lambda event: on_move('left'))
    root.bind("<Right>", lambda event: on_move('right'))
    root.bind("<Up>", lambda event: on_move('up'))
    root.bind("<Down>", lambda event: on_move('down'))


    root.mainloop()

game_play_gui()
