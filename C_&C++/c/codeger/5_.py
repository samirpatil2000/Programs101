import sys
from sys import stdin, stdout


# def get_ints(): 
    # return map(int, sys.stdin.readline().strip().split()) 


def getMatrix():
    C=int(stdin.readline())
    R=2*C-1
    mat=[[None for _ in range(C)] for i in range(R)]
    for i in range(R): 
        arr = [int(x) for x in stdin.readline().split()]
        for k in range(len(arr)):
            mat[i][k]=arr[k]
    print(mat)
    return mat
    
mat_=getMatrix()


def function(mat_):
    for i in range(len(mat_)):
        if(i<len(mat_)-1):
            x=mat_[i+1][0]-mat_[i-1][0]
            print(x)
    
    
    return

function(mat_)