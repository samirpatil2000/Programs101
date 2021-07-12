

def buyAndSell(arr):
    buy=0
    sell=0
    profite_=0
    
    for i in range(len(arr)-1):
        if arr[sell]<=arr[i]:
            sell+=1
        else:
            profite_+=(arr[sell]-arr[buy])
            buy=sell=i
    profite_+=(arr[sell]-arr[buy]) 
    return profite_

arr=[10,15,17,20,16,18,22,20,22,20,23,25]
print(buyAndSell(arr))