def grid_to_string(grid, n):
    grid1 = ""
    for ligne in grid:
        grid1 += "\n" + " ==="*n + "\n|"
        for tile in ligne:
            grid1 = grid1 + ' ' + str(tile) + ' |'
    grid1 += "\n" + " ==="*n + "\n"
    return grid1[1:-1]