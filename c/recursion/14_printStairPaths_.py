def printStairPaths(n,output_str):
    if(n==0):
        print(output_str)
        return
    if(n<0):
        return
    printStairPaths(n-1,output_str+"1");
    printStairPaths(n-2,output_str+"2");
    printStairPaths(n-3,output_str+"3");
    
printStairPaths(10,"")