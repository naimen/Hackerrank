#!/usr/bin/python
from math import sqrt
# Head ends here
def next_move(posr, posc, board):
    
    cells=scan(board)
    d = choose(posr,posc,cells)
    diffr = posr-d[0]
    diffc = posc-d[1]
    
    if diffc == 0 and diffr == 0:
        print("CLEAN")
    elif diffr == 0:
        print(movehorizontal(diffc)) 
    elif diffc ==0:
        print(moveverticaly(diffr))
    else:
        print(movehorizontal(diffc))
        
def scan(board):
    cells =[]
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 'd':
                cells.append((i,j))
    return cells

def choose(posr,posc,cells):
    dists=[]
    for c in cells:
        x=(posr-c[0])**2
        y=(posc-c[1])**2
        dist = sqrt(x+y)
        dists.append(dist)
    return cells[dists.index(min(dists))]

def movehorizontal(diffc):
    if diffc < 0:
        return "RIGHT"
    else: return "LEFT"

def moveverticaly(diffr):
    if diffr < 0:
        return "DOWN"
    else: return "UP"

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
