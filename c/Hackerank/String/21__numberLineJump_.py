
import sys
def funt(x,v1,y,v2):
    if(x<y and v1<=v2):
        return "NO"
    while(x!=y):
        
        x+=v1
        y+=v2
        if(x>y):
            return "NO"
    if(x==y):
        return "YES"
  

def get_ints(): 
    return map(int, sys.stdin.readline().strip().split()) 

a,b,c,d =get_ints()
print(funt(a,b,c,d))