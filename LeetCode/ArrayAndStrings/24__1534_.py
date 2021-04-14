def countGoodTriplets(arr, a, b, c):
    len_=len(arr)
    count=0
    for i in range(len_):
        for j in range(i+1,len_):
            for k in range(j+1,len_):
                if(abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c):
                    count+=1
    return count



arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr,a,b,c))
        
    