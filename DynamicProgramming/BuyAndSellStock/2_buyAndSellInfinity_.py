

def buyAndSell(arr):
    buy=0
    sell=0
    profite_=0
    
    for i in range(len(arr)):
        if arr[sell]<=arr[i]:
            sell+=1
        else:
            profite_+=(arr[sell]-arr[buy])
            buy=sell=i
    profite_+=(arr[sell]-arr[buy]) 
    return profite_