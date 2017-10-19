from enum import Enum
from operator import sub
from random import randrange
class Orientation(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

class Bot():
    def __init__(self,player,view):
        self.player = player
        self.view = view
    
    def step(self):
        free, card = self.scan(self.view, '-')
        exit,_ = self.scan(self.view, 'e')
        if exit:
            print(exit[0].value)
        else:
            if card == 8:
                if Orientation.UP not in free or Orientation.RIGHT not in free:
                    print('LEFT')
                elif Orientation.LEFT not in free:
                    print('DOWN')
                else: print(free[0].value)
            elif card == 6:
                if Orientation.DOWN not in free:
                    print('LEFT')
                elif Orientation.UP not in free:
                    print('RIGHT')
                else: print(free[0].value)
            else:
                print(free[0].value)
                
    def scan(self,board, _type):
        cells=[]
        card = 0
        bot = (1,1)
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == _type:
                    cell = (i,j)
                    diff = tuple(map(sub,bot,cell))
                    #print(diff)
                    if diff[0] == 0 and diff[1] == 1:
                        cells.append(Orientation.LEFT)
                    elif diff[0] == 0 and diff[1] == -1:
                        cells.append(Orientation.RIGHT)
                    elif diff[0] == 1 and diff[1] == 0:
                        cells.append(Orientation.UP)
                    elif diff[0] == -1 and diff[1] == 0:
                        cells.append(Orientation.DOWN)
                    card += 1
        #print(cells,card)
        return cells, card       
        
if __name__ == "__main__": 
    player = [int(i) for i in input().strip().split()] 
    view = [[j for j in input().strip()] for i in range(3)]
    agent = Bot(player,view)
    agent.step()
