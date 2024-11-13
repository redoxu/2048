THEMES = {"0": {"name": "Default", 0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: " ", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: " ", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def grid_to_string(grid, n):
    grid1 = ""
    for ligne in grid:
        grid1 += "\n" + " ==="*n + "\n|"
        for tile in ligne:
            grid1 = grid1 + ' ' + str(tile) + ' |'
    grid1 += "\n" + " ==="*n + "\n"
    return grid1[1:-1]

def long_value(grid):
    max = 0
    for ligne in grid:
        for tile in ligne:
            c = len(str(tile))
            if c > max:
                max = c
    return max

def grid_to_string_with_size(grid,n):
    grid1 = ""
    max = long_value(grid)
    for ligne in grid:
        grid1 += "\n" + (" "+"="*max)*n + "\n|"
        for tile in ligne:
            grid1 = grid1 + str(tile) + ' '*(max-len(str(tile))) + '|'
    grid1 += "\n" + (" "+"="*max)*n + "\n"
    return grid1[1:-1]

def grid_with_theme(grid, theme):
    n = len(grid)
    grid1 = [[' ' for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            grid1[i][j] = theme[grid[i][j]]
    return grid1

def long_value_with_theme(grid, theme):
    return long_value(grid_with_theme(grid, theme))

def grid_to_string_with_size_and_theme(grid, theme, n):
    return grid_to_string_with_size(grid_with_theme(grid, theme), n)
