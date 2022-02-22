"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import os.path
from patterns_configurations import *

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def readFile(grid:np.ndarray, f: str):
    dataFile = open(f, 'r')
    data = dataFile.readlines()
    data.pop(0)
    for line in data:
        cell = line.split(' ')
        x = int(cell[0])
        y = int(cell[1])
        grid[x][y] = ON
    return grid


def neighbors(grid,i,j):
    sum=0
    for x in range(-1,2):
        for y in range(-1,2):
            try:
                sum+=grid[i+x][j+y]
            except:
                pass
    sum-=grid[i][j]
    return sum/ON

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    for x in range(0,N):
        for y in range(0,N):
            cell=grid[x][y]
            check=neighbors(grid,x,y)
            #Any live cell with two or three live neighbours lives on to the next generation
            if(cell==ON and (2<=check<=3)):
                cell=ON
            #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
            elif(cell==OFF and check==3):
                cell=ON
            #Any live cell with more than three live neighbours dies, as if by overpopulation
            #Any live cell with fewer than two live neighbours dies, as if by underpopulation
            else:
                cell=OFF
            newGrid[x][y]=cell
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    parser.add_argument('--universe-size', dest='N', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    args = parser.parse_args()
    # set grid size
    N = 60
    if args.N and int(args.N) > 9:
        N = int(args.N)

    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    # Uncomment lines to see the "glider" demo
    fileName = 'data.txt'

    """
        if(os.path.isfile(fileName)):
        dataFile = open(fileName, 'r')
        data = dataFile.read()
        h = int(data.split()[0])
        v = int(data.split()[1])
        grid = np.zeros(h*v).reshape(h, v)
        grid = readFile(grid, fileName)
    else:
        grid = np.zeros(N*N).reshape(N, N)
        grid = randomGrid(N)
    """

    grid = np.zeros(N*N).reshape(N, N)

  
    if(os.path.isfile(fileName)):
        grid = readFile(grid, fileName)
    else:
        grid = randomGrid(N)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()

# call main
if __name__ == '__main__':
    main()