


def missing(arr,brr):
    i=j=0
    list_=[]
    while(i<len(arr) and j<len(brr)):
        if (arr[i]!=brr[j]):
            list_.append(brr[j])
            j+=1
        else:
            i+=1
            j+=1
    # print(j,"j")
    while(j<len(brr)):
        print(brr[j])
        list_.append(brr[j])
        j+=1
    while(i<len(arr)):
        print(arr[i])
        list_.append(arr[i])
        i+=1
    
        
        
        
    print(list_)
    
    
# arr=[203 ,204 ,205 ,206 ,207 ,208 ,203 ,204 ,205 ,206]
# brr=[203 ,204 ,204 ,205 ,206 ,207 ,205 ,208 ,203 ,206 ,205, 206, 204]

# n = int(input())

arr = [i for i in range(0,10)]

# m = int(input())

brr = [i for i in range(0,12)]



arr.sort()
brr.sort()
print(arr)
print(brr)
missing(arr,brr)