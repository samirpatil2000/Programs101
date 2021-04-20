
def function(n,queries):
    arr=[0 for _ in range(n)]
    max_=0
    for i in range(len(queries)):
        for j in range(queries[i][0],queries[i][1]+1):
            arr[j-1]+=queries[i][2]
            max_=max(arr[j-1],max_)
        print(arr)
    return max(arr),max_


# queries=[[1, 2, 100],[2, 5, 100],[3, 4, 100]]
queries=[[1 ,5 ,3],[4 ,8 ,7],[6 ,9 ,1]]
n=10
print(function(n,queries))
    