from math import *
import logging,sys
from random import randrange
from random import random
from random import choice

logging.basicConfig(format='%(message)s',level=logging.DEBUG)
def fire(N,grid):    
    potentialtarget = []
    hit = []
    empty = 0
    adjacent_hit=set()
    weights = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'h':
                hit.append((i,j))
            elif grid[i][j] == '-':
                weights[i][j] = calc_weight(i,j,grid)
                potentialtarget.append((i,j))
                empty += 1
    
    #logging.debug(repr(potentialtarget))
    #for i,v in enumerate(weights):
    #    logging.debug(repr(i)+repr(v))
    
    if hit:
        for h in hit:
            adjacent = get_adjacent(h[0],h[1])
            adjacent_hit.update(adjacent)
        for i in adjacent_hit.copy():
            if grid[i[0]][i[1]] != '-':
                adjacent_hit.remove(i)
        if len(hit)>=2:
            adjacent_hit = prune(hit,adjacent_hit)
        target = choice(list(adjacent_hit))
    
    elif randrange(empty) < 40 :
        target = choose_max(weights)
    else: 
        target = choice(potentialtarget)

    print(target[0],target[1])

def get_adjacent(x,y,N=10):
    left = (max(0, min(x-1, N-1)),y)
    right = (max(0, min(x+1, N-1)),y)
    up = (x,max(0, min(y-1, N-1)))
    down = (x,max(0, min(y+1, N-1)))
    
    return[left,right,up,down] 

def is_adjacent(a,b):
    return a[0]==b[0] or a[1]==b[1]

def calc_weight(x,y,grid):
    weight = 0
    lowx = max(0, min(x-1, N-1))
    highx = max(0, min(x+1, N-1))
    lowy = max(0, min(y-1, N-1))
    highy = max(0, min(y+1, N-1))
    
    for i in range(lowx,highx):
        for j in range(lowy,highy):
            if grid[i][j] == '-':
                weight += 1
    return weight

def choose_max(weights):
    x = argmax(list(map(max,weights)))
    y = argmax(weights[x])
    return (x,y)

def argmax(x):
    return x.index(max(x))

def prune(hit,_adjacent_hit):
    adjacent_hit = _adjacent_hit
    diffx = 0
    diffy = 0
    temp = hit[0]
    for h in hit:
        diffx = h[0]-temp[0]
        diffy = h[1]-temp[1]
        temp=h
    
    if diffx !=0:
        for a in adjacent_hit.copy():
            if hit[0][1] != a [1]:
                adjacent_hit.remove(a)      
    else:
        for a in adjacent_hit.copy():
            if hit[0][0] != a[0]:
                adjacent_hit.remove(a)
    return adjacent_hit
                        
if __name__ == '__main__':
    N = int(input().strip().split()[0])
    grid = [[i for i in str(input().strip())] for _ in range(N)] 
    fire(N,grid)