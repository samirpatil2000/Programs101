
def fun(x:int,y:int):
    if max(x,y)==x:#max row
        if x&1:
            print((x-1)**2+y-1+1)
        else:
            print(x**2-(y-1))
    else:
        if y&1:
            print(y**2-(x-1))
        else:
            print((y-1)**2+x-1+1)
      
t=int(input())
while t:
    t-=1
    x,y=input().split(' ')
    fun(int(x),int(y))
    

# fun(4,3)