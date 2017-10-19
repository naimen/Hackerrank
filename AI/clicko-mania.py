#!/bin/python
from math import *
import logging,sys
from random import randrange

logging.basicConfig(format='%(message)s',level=logging.DEBUG)

def nextMove(width, height, color, grid):
    weights = [[-1 for _ in range(height)] for _ in range(width)]
    for x in range(width):
        for y in range(height):
            if grid[x][y] is not '-':
                weights[x][y] = calcWeights(x,y,grid,color)
    
    for i,v in enumerate(weights):
        logging.debug(repr(i)+repr(v))
    
    #approx the density of the same color
    rowsum = []
    for x in weights:
        rowsum.append(sum(x))
    colsum = []
    weights_T = list(zip(*weights))
    for y in weights_T:
        colsum.append(sum(y))

    #choose a target based on row
    temp_x = argmax(rowsum)
    temp_y = argmax(weights[temp_x])
    rowtarget = (temp_x, temp_y)
    #choose a target based on col
    temp_y = argmax(colsum)
    temp_x = argmax(weights_T[temp_y])
    coltarget = (temp_x,temp_y)
    
    #the maximal weight without considering density
    temp_x = argmax(list(map(max,weights)))
    temp_y = argmax(weights[temp_x])
    #logging.debug(temp_x)
    logging.debug(repr(temp_x)+" "+repr(temp_y))
    maxitarget = (temp_x,temp_y)
    
    #the output is the maximum weight between col target and row target
    if weights[rowtarget[0]][rowtarget[1]] > weights[coltarget[0]][coltarget[1]]:
        output = rowtarget
    else: output = coltarget
    
    #with chance of 1/2, choose the maxitarget    
    if weights[maxitarget[0]][maxitarget[1]] > weights[output[0]][output[1]] and randrange(0,2) > 0: 
        output = maxitarget
    
    if color <= 3: #hack based on board
        output = rowtarget
    
    print (output[0],output[1])

def calcWeights(posx,posy,grid,colors):
    lowx= posx-1
    highx = posx+2
    lowy=posy-1
    highy=posy+2
    
    if posx == 0:
        lowx = 0
    if posy == 0:
        lowy = 0
    if posx == len(grid)-1:
        highx = len(grid)
    if posy == len(grid[posx])-1:
        highy = len(grid[posx])        
    
    color = grid[posx][posy]
    weight = 0
    #calc the weights in a view of 3*3
    for i in range(lowx,highx):
        for j in range(lowy,highy):
            if color == grid[i][j] and adjacent((i,j),(posx,posy)):
                if colors <= 3: #hack based on board
                    weight += 1
                else:   
                    weight += (f_inc(i)+f_desc(j))
    return weight

def adjacent(a,b):
    if a[0] == b[0] or a[1]==b[1]:
        return True
    else: 
        return False

def argmax(x):
    return x.index(max(x))

def f_inc(y):
    return log(y+2)

def f_desc(x):
    return -log(x+2)+3

if __name__ == '__main__':
    x,y,k = [ int(i) for i in input().strip().split() ] 
    grid = [[i for i in str(input().strip())] for _ in range(x)] 
    nextMove(x, y, k, grid)
