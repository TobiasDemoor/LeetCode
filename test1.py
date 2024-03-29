#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reachTheEnd' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER maxTime
#

def reachTheEnd(grid, maxTime):
    n = len(grid)
    m = len(grid[0])

    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 0

    i, j = 0, 0
    queue = {(i, j)} 
    minTime = -1

    while queue: 
        [i, j] = queue.pop() 
        time = visited[i][j]

        # we've reached the end 
        if i == n-1 and j == m-1:
            if time <= maxTime: return 'Yes'
            if time < minTime or minTime == -1: minTime = time
            continue

        # we are not in the last row and we can move down and we haven't visited the cell below
        if i < n-1 and grid[i+1][j] == '.':
            if visited[i+1][j] == -1 or visited[i+1][j] > time + 1: 
                queue.add((i+1, j)) 
                visited[i+1][j] = time + 1

        # we are not in the last column and we can move right and we haven't visited the cell to the right
        if j < m-1 and grid[i][j+1] == '.':
            if visited[i][j+1] == -1 or visited[i][j+1] > time + 1: 
                queue.add((i, j+1)) 
                visited[i][j+1] = time + 1

        # we are not in the first row and we can move up and we haven't visited the cell above
        if i > 0 and grid[i-1][j] == '.':
            if visited[i-1][j] == -1 or visited[i-1][j] > time + 1: 
                queue.add((i-1, j)) 
                visited[i-1][j] = time + 1

        # we are not in the first column and we can move left and we haven't visited the cell to the lefts
        if j > 0 and grid[i][j-1] == '.':
            if visited[i][j-1] == -1 or visited[i][j-1] > time + 1: 
                queue.add((i, j-1)) 
                visited[i][j-1] = time + 1
    
    if minTime > -1 and minTime <= maxTime:
        return 'Yes'
    else:
        return 'No'
            

  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_count = int(input().strip())

    grid = []

    for _ in range(grid_count):
        grid_item = input()
        grid.append(grid_item)

    maxTime = int(input().strip())

    result = reachTheEnd(grid, maxTime)

    fptr.write(result + '\n')

    fptr.close()