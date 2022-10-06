# input via readline method
import sys
from sys import stdin, stdout

n = stdin.readline()

# array input similar method
arr = [int(x) for x in stdin.readline().split()]

arr=[[ None for m in range(k)] for k in range(5)]


def get_ints(): 
    return map(int, sys.stdin.readline().strip().split()) 


a,b,c,d = get_ints()


# list=[i.replace("'","") for i in list]
def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))
 
Arr = get_ints()


def get_string(): return sys.stdin.readline().strip()
 
string = get_string()


def getMatrix():
    R,C=get_ints()
    mat=[[None for _ in range(C)] for i in range(R)]
    for i in range(R): 
        arr = [int(x) for x in stdin.readline().split()]
        for k in range(len(arr)):
            mat[i][k]=arr[k]
    print(mat)
    
x=['6','2']


# for i in range(len(x)):
# x=