

import sys
from sys import stdin, stdout
from typing import Counter

t = int(stdin.readline())
def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())
def get_string(): 
    return sys.stdin.readline().strip()


for j in range(t):     
    N,K = get_ints()
    S=get_string()
    i=1
    count=0
    while(i <= N//2):
        if(S[i-1]!=S[N-i+1-1]):
            count+=1
        i+=1
    # print(S,K,count)
    print("Case #"+str(j)+":",K-count)
    
        
    
    