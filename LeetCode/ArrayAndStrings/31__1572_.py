def diagonalSum(mat):
    row=col=0
    sum=0
    while(row < len(mat) and col < len(mat[0])):
        sum+=mat[row][col]
        if(row!=len(mat[0])-1-row):
            sum+=mat[len(mat[0])-1-row][col]
        row+=1
        col+=1
    return sum
mat = [[5]]
print(diagonalSum(mat)) 