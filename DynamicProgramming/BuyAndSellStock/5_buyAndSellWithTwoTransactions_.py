
def fun(arr):
    reverse_Arr=arr.copy()
    reverse_Arr_2=arr.copy()
    min_buy=arr[0]
    max_profite_1=0
    
    for i in range(len(arr)):
        min_buy=min(min_buy,arr[i])
        max_profite_1=max(max_profite_1,arr[i]-min_buy)
        reverse_Arr[i]=max_profite_1
        
    max_sell=arr[len(arr)-1]
    max_profite_2=0
    for i in range(len(arr)-1,-1,-1):
        max_sell=max(max_sell,arr[i])
        max_profite_2=max(max_profite_2,max_sell-arr[i])
        reverse_Arr_2[i]=max_profite_2
        
    print(reverse_Arr)
    print(reverse_Arr_2)

arr=[3,10,20,30,50,30]  
fun(arr)