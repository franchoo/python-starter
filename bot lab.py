id = int(input())
grid = [] 
for i in range(0, 3): 
    grid.append(input().strip())

    moves=('UP', 'DOWN', 'LEFT', 'RIGHT')
    steps=((-1,0), (1,0), (0,-1), (0,1))
    positions={}
    for x in range(0,n):
        for y in range(0,n):
            positions[grid[x][y]]=[x,y]
    post=positions['m']
    dest=positions['p']
    while post != dest:
        V, H = dest[0]-post[0], dest[1]-post[1]
        flow=(int(V>0), int(H>0)+2)[abs(V) < abs(H)]
        post=[post[0]+steps[flow][0], post[1]+steps[flow][1]]
        print(moves[flow])
