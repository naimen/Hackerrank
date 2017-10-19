#!/usr/bin/python
def displayPathtoPrincess(n,grid):
#print all the moves here
    m = [int(n/2),int(n/2)]
    p = [0,0]
    #res = []
    if grid[0][-1] == 'p':
        p= [0,n-1]
    elif grid[-1][0] == 'p':
        p= [n-1,0]
    elif grid[-1][-1] == 'p':
        p= [n-1,n-1]
    
    h=m[0]-p[0]
    v=m[1]-p[1]
    
    if h < 0:
        for i in range(0,abs(h)):
            #res.append('RIGHT')
            print('RIGHT')
    else:
        for i in range(0,abs(h)):
            #res.append('LEFT')
            print('LEFT')
    if v < 0:
        for i in range(0,abs(v)):
            #res.append('DOWN')
            print('DOWN')
    else:
        for i in range(0,abs(v)):
            #res.append('UP')
            print('UP')
        
        
        


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
