


def buyAndSellStocksWithCoolDown(arr,fees):
    bsp=arr[0]
    ssp=0
    csp=0
    
    for i in range(1,len(arr)):
        print(bsp,ssp,csp)
        pre_bsp=bsp
        pre_ssp=ssp
        bsp=min(bsp,arr[i]-csp)
        ssp=max(ssp,arr[i]-pre_bsp)
        csp=max(pre_ssp,csp)
        

arr=[10,15,17,20,16,18,22,20,22,20,23,25]
print(buyAndSellStocksWithCoolDown(arr,3))
    
    