def nextMove(n,r,c,grid):
    p=(-1,-1)
    for i in range(0,n):
        for j in range(0,n):
            if(grid[i][j]=='p'):
                p=(i,j)    
    
    diffr = r - p[0]
    diffc = c - p[1]
    
    if diffr == 0:
        return movehorizontal(diffc)
    elif diffc ==0:
        return moveverticaly(diffr)
    else:
        return movehorizontal(diffc)
        
def movehorizontal(diffc):
    if diffc < 0:
        return "RIGHT"
    else: return "LEFT"

def moveverticaly(diffr):
    if diffr < 0:
        return "DOWN"
    else: return "UP"


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
