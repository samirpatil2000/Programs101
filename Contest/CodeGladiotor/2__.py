from sys import stdin
from math import sqrt
def primeDiff(L,R):
    prime_arr=[True]*(R+1)
    prime_arr[0]=prime_arr[1]=False
    p = 2
    while (p * p <= R):
        if (prime_arr[p] == True):                
            for i in range(p * 2, R + 1, p):
                prime_arr[i] = False
        p += 1
                
    arr=[]
    
    for i in range(R,L-1,-1):
        if prime_arr[i]==True:
            arr.append(i)
            break
    for i in range(L,R+1):
        if prime_arr[i]==True:
            arr.append(i)
            break
    if len(arr)==2:
        return max(arr)-min(arr)
    elif len(arr)==1:
        return 0
    else:
        return -1
    
            
        
    return arr

# L,R=5,11
# print(primeDiff(L,R))   
            


def main():
    t=int(input())
    
    while t:
        t-=1
        L,R=[int(i) for i in stdin.readline().split()]
        print(primeDiff(L,R))
        
# main()
print(primeDiff(4,5))
        
        
        