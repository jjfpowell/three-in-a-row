import numpy as np
grid=np.array([[3, 3, 3], [3, 3, 3],[3, 3, 3]])

def winner():
    for ply in range(1,3):
        for r in range(3):
            if grid[r][0]==grid[r][1]==grid[r][2]==ply:
                return ply
        for c in range(3):
            if grid[0][c]==grid[1][c]==grid[2][c]==ply:
                return ply
        if grid[0][0]==grid[1][1]==grid[2][2]==ply:
            return ply
        if grid[0][2]==grid[1][1]==grid[2][0]==ply:
            return ply
    if (grid!=0).all():
        print("Tie")

winner()