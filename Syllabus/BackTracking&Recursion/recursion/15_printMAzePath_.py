def printMazePath(n,m,d1,d2,output_str):
    if(n>d1-1 or m>d2-1):
        return
    if(n==d1-1 and m==d2-1):
        print(output_str)
        return
    if(n<d1):
        printMazePath(n,m+1,d1,d2,output_str+"h")
    if(m<d2):
        printMazePath(n+1,m,d1,d2,output_str+"v")
    
printMazePath(0,0,8,1,"")