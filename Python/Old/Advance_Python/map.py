

def iseven(n):
    if n%2==0:
        return True

def square(n):
    return n*n

def filter(function,list):
    l=[]
    for i in list:
        if function(i):
            l.append(i)
    return l

e=list(map(square,filter(iseven,range(100))))
print(e)



sam=[(x,y,z) for x in range(1,100) for y in range(x,100) for z in range(y,100) if x*x+y*y==z*z ]
print(sam)