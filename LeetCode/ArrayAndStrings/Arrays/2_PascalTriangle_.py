from typing import List


def generate(numRows):
    arr=[[ None for m in range(k)] for k in range(1,numRows+1)]
    print(arr)
    arr[0][0]=1
    for i in range(1,numRows):
        arr[i][0]=1
        j=1
        while(j<i):
            arr[i][j]=arr[i-1][j]+arr[i-1][j-1]
            j+=1
        arr[i][j]=1
    return arr
print(generate(5))


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1]*(i+1) for i in range(numRows)]
        # print(triangle)
        
        for row in range(2,numRows):
            for col in range(1,row):
                triangle[row][col]=triangle[row-1][col-1]+triangle[row-1][col]
        
        return triangle
        
sol=Solution()
print(sol.generate(1))