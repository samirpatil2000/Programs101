
import sys
from sys import stdin, stdout


def fn(mat,row,col):
    count=0
    for i in range(row):
        for j in range(col-1):
            if(j<col and abs(mat[i][j]-mat[i][j+1])>1):
                if(mat[i][j]>mat[i][j+1]):
                    temp=mat[i][j+1]
                    mat[i][j+1]+=abs(mat[i][j]-mat[i][j+1])-1
                    count+=(mat[i][j+1]-temp)
                else:
                    temp=mat[i][j]
                    mat[i][j]+=abs(mat[i][j]-mat[i][j+1])-1
                    count+=(mat[i][j]-temp)
    for j in range(col):
        for i in range(row-1):
            if(abs(mat[i][j]-mat[i+1][j])>1):
                if(mat[i][j]>mat[i+1][j]):
                    temp=mat[i+1][j]
                    mat[i+1][j]+=abs(mat[i][j]-mat[i+1][j])-1
                    count+=(mat[i+1][j]-temp)
                else:
                    temp=mat[i][j]
                    mat[i][j]+=abs(mat[i][j]-mat[i+1][j])-1
                    count+=(mat[i][j]-temp)
    return count



t = int(stdin.readline())
def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())


for i in range(t):
    R,C=get_ints()
    mat=[[None for _ in range(C)] for _ in range(R)]
    for i in range(R): 
        arr = [int(x) for x in stdin.readline().split()]
        for k in range(len(arr)):
            mat[i][k]=arr[k]
    x=fn(mat,R,C)
    print("Case #"+str(i+1)+":",x)



"""
3
1 3
3 4 3
1 3
3 0 0
3 3
0 0 0
0 2 0
0 0 0
"""