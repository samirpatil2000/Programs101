
from typing import Counter


arr=[1,2,5,10,20,50,100,200,500,2000]

def numberofMinCoins(arr,X):
    arr.reverse()
    i=0
    coins=[]
    while(X>=0):
        if i<len(arr) and arr[i]<=X:
            X=X-arr[i]
            coins.append(arr[i])
        else:
            i+=1
        if X==0:
            return coins


print(numberofMinCoins(arr,594))
    
