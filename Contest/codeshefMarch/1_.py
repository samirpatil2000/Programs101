import sys
from sys import stdin,stdout


def get_ints(): 
    return map(int, sys.stdin.readline().strip().split()) 
N,H,x = get_ints()


def get_arr(): 
    return list(map(int, sys.stdin.readline().strip().split()))
arr = get_arr()


def fun(arr,N):
    for i in range(N):
        if(arr[i]+x>=H):
            print("Yes")
            return
    print("NO")
    return
    
fun(arr,N)