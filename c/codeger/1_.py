#inception
import sys
from sys import stdin, stdout


def get_ints(): 
    return map(int, sys.stdin.readline().strip().split()) 

n = int(stdin.readline())
# n=2
while(n>0):
    P,Q=get_ints()
    print(P-Q)
    n-=1
    
