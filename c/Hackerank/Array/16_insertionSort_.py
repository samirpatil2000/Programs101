
def printNum(n,arr):
    for i in range(n):
        print(arr[i],end=" ")

def insertion(n,arr):
    if(n==1):
        printNum(n,arr)
        print()
        return
    # elif(n==2):
    #     if(arr[1]<arr[0]):
    #         print(str(arr[1])+" "+str(arr[0]))
    #     else:
    #         printNum(2,arr)
    else:
        i=n-2
        temp=arr[n-1]
        while(i>=0 and temp<=arr[i]):
            arr[i+1]=arr[i]
            i-=1
            printNum(n,arr)
            print()
        arr[i+1]=temp
        printNum(n,arr)
        print()
    
    
# n=5
# arr=[2, 4, 6, 8, 0]
n=2
arr=[1,0]

insertion(n,arr)


    