#!/bin/python3
def nextMove(posr, posc, board):
    d =scan(board)
    diffr = posr-d[0]
    diffc = posc-d[1]
    
    if diffc == 0 and diffr == 0:
        print("CLEAN")
    elif diffc ==0:
        print(moveverticaly(diffr))
    else:
        print(movehorizontal(diffc))
        
def scan(board):
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == 'd':
                return (i,j)
    

def movehorizontal(diffc):
    if diffc < 0:
        return "RIGHT"
    else: return "LEFT"

def moveverticaly(diffr):
    if diffr < 0:
        return "DOWN"
    else: return "UP"

    
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
