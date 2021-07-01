''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdin, stdout
from typing import Dict
import math
# n = stdin.readline()

# array input similar method
# def sol(n:int,memo={})->int:
#     if n in memo:return memo[n]
#     if n==0 or n==1 or n==2:
#         return 1
#     # print(n)
#     if n%2!=0:
#         memo[n]=sol(n//2,memo)+sol(n//2+1,memo)
#         return memo[n]
#     else:
#         memo[n]=sol(n//2)
#         return memo[n]
count_=0 
def sol(n:int,m:int)->int:
    global count_
    return 
    
    
def sol2(n:int,memo={})->int:
    count_=0
    i_=0
    
    for i in range(2,n//2+1):
        if n%i==0:
            count_=max(count_,sol(n//i)+n)
            i_+=i
            print(count_,i_,i)
            
    
    
        
    
    

def main():
    t=int(input())
    arr = [int(x) for x in stdin.readline().split()]
    sum_=0
    for i in arr:
        sum_+=sol(i)
    print(sum_)
    
 # Write code here 

# main()

# print(sol(6))
# print(11//2,11//2+1)
sol2(6)
