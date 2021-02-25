

def getMazePaths(row,col,dr,dc):
    if(row==dr and col==dc):
        return " "
    p1=[]
    p2=[]
    p3=[]
    
    j=1
    paths=[]
    while(j<=3):
        if(row<dr):    
            p2=getMazePaths(row+j,col,dc,dr)
        if(col<dc):
            p1=getMazePaths(row,col+j,dc,dr)
        if(row<dr and col<dc):
            p3=getMazePaths(row+j,col+j,dc,dr)
        str_j=str(j)
        for i in p1:
            paths.append("h"+str_j+i)
        for i in p2:
            paths.append("v"+str_j+i)
        for i in p3:
            paths.append("d"+str_j+i)
        j+=1
    return paths

print(getMazePaths(0,0,2,2))