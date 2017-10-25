from math import *
import logging,sys
from random import randrange
from random import random
from random import choice

logging.basicConfig(format='%(message)s',level=logging.DEBUG)
def nextMove(N,grid):    
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

def placeShips(ss,dd,ca,bb,cv):
    res = []
    bound = 10
    sub_res = []
    pos = [(x,y) for x in range(bound) for y in range(bound)]
    
    cv_pos, invalid = place_cv(pos)
    for i in invalid:
        pos.remove(i)
    bb_pos, invalid = place_bb(pos)
    for i in invalid:
        pos.remove(i)
    ca_pos, invalid = place_ca(pos)
    for i in invalid:
        pos.remove(i)
    
    
    for i in range(ss):
        sub_p = choice(pos)
        sub_res.append(sub_p)
        pos.remove(sub_p)
    
    for i in range(dd):
        dd = place_dd(pos)
        pos.remove(dd[0])
        pos.remove(dd[1])
        res.append(dd)
    res.append(ca_pos)
    res.append(bb_pos)
    res.append(cv_pos)
    
    logging.debug(repr(res))
    
    for i in sub_res:
        print(i[0],i[1])
    
    for i in res:
        print("{} {}:{} {}".format(i[0][0],i[0][1],i[1][0],i[1][1]))
def place_cv(pos):
    if randrange(2) > 0:
        res = ((0,2),(0,6))
        invalid = [(0,x) for x in range(2,7)]
    else:
        res = ((9,3),(9,7))
        invalid = [(9,x) for x in range(3,8)]
    
    return res,invalid        

def place_bb(pos):
    if randrange(2) > 0:
        res = ((1,0),(4,0))
        invalid = [(x,0) for x in range(1,5)]
    else:
        res = ((5,9),(8,9))
        invalid = [(x,9) for x in range(5,9)]
    
    return res,invalid

def place_ca(pos):
    if randrange(2) > 0:
        res = ((6,0),(8,0))
        invalid = [(x,0) for x in range(6,9)]
    else:
        res = ((1,9),(3,9))
        invalid = [(x,9) for x in range(1,4)]
    
    return res,invalid
        
def place_dd(pos):
    orient = [-1,1]
    
    dd_ps = choice(pos)
    if randrange(2) > 0:
        dd_pe = (dd_ps[0],dd_ps[1]+1*choice(orient))
    else:
        dd_pe = (dd_ps[0]+1*choice(orient),dd_ps[1])
    res = (dd_ps,dd_pe)
    
    if dd_pe not in pos:
        res = place_dd(pos)
    
    return res

if __name__ == '__main__':
    if input() == 'INIT':
        placeShips(2,2,1,1,1)
    else:
        N = 10
        grid = [[i for i in str(input().strip())] for _ in range(N)] 
        nextMove(N,grid)