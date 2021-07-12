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