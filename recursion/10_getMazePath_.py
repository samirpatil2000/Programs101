

def getMazePaths(row,col,dr,dc):
    if(row==dr-1 and col==dc-1):
        return " "
    p1=[]
    p2=[]
    if(row<dr):    
        p2=getMazePaths(row+1,col,dc,dr)
    if(col<dc):
        p1=getMazePaths(row,col+1,dc,dr)
    
    paths=[]
    for i in p1:
        paths.append("h"+i)
    for i in p2:
        paths.append("v"+i)
    return paths

print(getMazePaths(0,0,10,10))