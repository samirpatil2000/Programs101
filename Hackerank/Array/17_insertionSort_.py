
def printNum(n,arr):
    for i in range(n):
        print(arr[i],end=" ")

def insertion(n,arr):
    if(n==1):
        printNum(n,arr)
        print()
        return
    else:
        for i in range(1,n):
            temp=arr[i]
            j=i-1
            while(j>=0 and temp<=arr[j]):
                arr[j+1]=arr[j]
                j-=1
                # printNum(n,arr)
                # print()
            arr[j+1]=temp
            printNum(n,arr)
            print()
    
    
# n=5
arr=[0]

# arr=[3 ,4 ,7, 5 ,6, 2 ,1]
n=len(arr)

insertion(n,arr)


    