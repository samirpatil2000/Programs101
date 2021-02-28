
def getStairPaths(n):
    
    if(n==0):
        return " "
    elif(n<0):
        return ""
    paths=[]
    p1=getStairPaths(n-1)
    p2=getStairPaths(n-2)
    p3=getStairPaths(n-3)
    for i in p1:
        paths.append("1"+i)
    for i in p2:
        paths.append("2"+i)
    for i in p3:
        paths.append("3"+i)
    return paths;

print(getStairPaths(5))