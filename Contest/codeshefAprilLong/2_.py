import sys
from sys import stdin,stdout




try:
    def get_ints(): 
        return map(float, sys.stdin.readline().strip().split())
    n = int(stdin.readline())
    while(n>0):
        n-=1
        k1,k2,k3,v = get_ints()
        k1=round(k1,1)
        k2=round(k2,1)
        k3=round(k3,1)
        v=round(v,2)
        # print(k1,k2,k3,v)
        if(round((100)/(k1*k2*k3*v),2) < 9.58):
            print("Yes")
        else:
            print("NO")
except:
    pass


"""
3
1.0 1.0 1.0 10.45
1.0 1.0 1.0 10.44
1.0 1.0 0.9 10.45
"""

# k1,k2,k3,v=1.0, 1.0 ,1.0 ,10.45
    # x=
    
    # print()