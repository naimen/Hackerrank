#!/usr/bin/python3
from math import sqrt
from random import randrange
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Cleanbot(metaclass=Singleton):
    
    def __init__(self):
        self.discovered = []
        self.visited = []
    
    def next_move(self,posr, posc, board):
        cells =self.scan(board,'d')   
        if cells:
            target = self.choose(posr,posc,cells)
            self.discovered = cells
        elif self.discovered:
            target = self.choose(posr,posc,self.discovered)
            self.discovered.remove(target)
        else:
            target = self.search(board)
            self.visited.append(target)

        diffr = posr-target[0]
        diffc = posc-target[1]   
        self.hunt(diffc,diffr)


    def scan(self,board, _type):
        cells=[]
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == _type:
                    cells.append((i,j))
        return cells

    def choose(self,posr,posc,cells):
        dists=[]
        for c in cells:
            x=(posr-c[0])**2
            y=(posc-c[1])**2
            dist = sqrt(x+y)
            dists.append(dist)
        return cells[dists.index(min(dists))]

    def search(self,board):
        cells = self.scan(board,'o')
        for v in self.visited:
            if cells.count(v):
                cells.remove(v)
        rand = randrange(0,len(cells))                
        return cells[rand]

    def hunt(self,diffc, diffr):
        if diffc == 0 and diffr == 0:
            print("CLEAN")
        elif diffc ==0:
            print(self.moveverticaly(diffr))
        else:
            print(self.movehorizontal(diffc))

    def movehorizontal(self,diffc):
        if diffc < 0:
            return "RIGHT"
        else: return "LEFT"

    def moveverticaly(self,diffr):
        if diffr < 0:
            return "DOWN"
        else: return "UP"




if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]
    agent = Cleanbot()
    agent.next_move(pos[0], pos[1], board)
