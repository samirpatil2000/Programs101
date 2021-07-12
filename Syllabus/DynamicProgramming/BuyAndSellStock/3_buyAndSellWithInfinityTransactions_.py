


def buyAndSellStocks(arr,fees):
    bsp=arr[0]
    ssp=0
    
    for i in range(1,len(arr)):
        print(ssp)
        old_bsp=bsp
        bsp=min(bsp,arr[i]-ssp)
        ssp=max(ssp,arr[i]-old_bsp-fees)
        
    return ssp


arr=[10,15,17,20,16,18,22,20,22,20,23,25]
print(buyAndSellStocks(arr,3))
    
    