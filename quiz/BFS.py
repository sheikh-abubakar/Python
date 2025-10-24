def bfs(cube):
    n=len(cube)
    m=len(cube[0])
    start=(0,0)
    goal=(n-1,m-1)
    if cube[0][0]==1 or cube[n-1][m-1]==1:
        return -1
    queue=[[start]]
    visited=[start]
    # (-1,0)->up
    # (0,1)->down
    # (0,-1)->left
    # (0,1)->right
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    while len(queue)>0:
        path=queue.pop(0)
        x,y=path[-1]
        if(x,y)==goal:
         return path
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            #cube[nx][ny] == 0 means the next cell is open (walkable)
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if cube[nx][ny]==0 and (nx,ny) not in visited:
                 new_path= path + [(nx,ny)]
                 queue.append(new_path)
                 visited.append((nx,ny))
    return -1
cube=[
 [0,0,1,1],
 [0,0,0,1],
 [0,1,0,0],
 [0,0,0,0]
]
result =bfs(cube)
if result !=-1:
   print("path found yahoooooooooooo",result)
else :
 print("ohhh! sorry path not found")