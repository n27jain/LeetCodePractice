# given mxn grid 
# you start at top left corner can can move only down one spot or to the right one spot
# how many ways can you arrive to the bottom right corner?
import numpy as np


def memo(m,n):
    matrix = np.zeros((m,n))
    return gridTraveler([m-1,n-1], m-1, n-1, matrix)


def gridTraveler(grid_size, m,n, matrix):
    if(matrix[m][n] != 0):
        return matrix[m][n]
    if(n <= grid_size[0] and m <= grid_size[1] and matrix[n][m] != 0 ): #check for flip condition
        return matrix[n][m]
        
    if(m == 0 or n == 0):
        return 1
    matrix[m][n] = gridTraveler(grid_size, m-1,n,matrix) + gridTraveler(grid_size, m,n-1,matrix)
    return matrix[m][n]
    
    
print(int(memo(3,3)),
int(memo(1,1)),
int(memo(18,18)))