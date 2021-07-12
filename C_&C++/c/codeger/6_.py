import sys
from sys import stdin, stdout

t = int(stdin.readline())


while(t>0):
    def get_ints(): 
        return map(int, sys.stdin.readline().strip().split()) 
    n,b = get_ints()
    sum_=0
    i=1
    while(sum_<b):
        sum_+=(i*n)
        i+=1
        # print()
    print(i-1)
    t-=1
    
    
    