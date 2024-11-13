from game2048 import grid_2048
import numpy as np

def move_row_left(row_grid):
    row = row_grid    
    for j in range(len(row)):
        for i in range(1,len(row)):
            if row[i-1]==0:
                row[i], row[i-1] =row[i-1], row[i]     
    for x in range(len(row)-1):
        if row[x]==row[x+1]:
            row[x]=2*row[x]
            row[x+1]=0
    for j in range(len(row)):
        for i in range(1,len(row)):
            if row[i-1]==0:
                row[i], row[i-1] =row[i-1], row[i]           
    return row
        
def move_row_right(grid_row):
    grid_row.reverse()
    grid = move_row_left(grid_row)
    grid.reverse()
    return grid 

def transpose(grid):
    grid_t = grid
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            grid_t[i][j] = grid_t[j][i]
    return grid_t 

def move_grid(grid,move):
    if move == "up":
        grid2=grid
        grid1 = transpose(grid)
        for i in range(len(grid)):
            grid2[i] = move_row_left(grid1[i])
        #grid2 = transpose(grid2)
        return transpose(grid2)
    if move == "down":
        grid1 = grid
        for i in range(len(grid[0])):
            grid1[i] = move_row_right(grid1[i])
        grid1 = transpose(grid1)
        return grid1
    if move == "right":
        grid1 = grid
        for i in range(len(grid[0])):
            grid1[i] = move_row_right(grid1[i])
        return grid1
    if move == "left":
        grid1 = grid
        for i in range(len(grid[0])):
            grid1[i] = move_row_left(grid1[i])
        return grid1
        
    
    