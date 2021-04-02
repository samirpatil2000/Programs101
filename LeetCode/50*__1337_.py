
# mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
mat= [[1,1,1,1,1],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,0],[1,1,1,1,1]]

k=3


def searchFun(mat_,row,left,right):
    mid=(left+right)//2
    # if(len(mat_)==0):
    #     return -1+1
    # if(len(mat_)==1):
    #     if(mat_[row][0]==1):
    #         return 0
    #     return -1+1
    if(left>right):
        return -1+1
    # print(row,mid+1)
    if(mid<len(mat_[0])-1 and mat_[row][mid]==1 and mat_[row][mid+1]==0):
        return mid+1
    else:
        if(mat_[row][mid]==0):
            return searchFun(mat_,row,0,mid-1)
        else:
            return searchFun(mat_,row,mid+1,right)
        
        
def kWeakestRows(mat_,k_):
    arr=[]
    print("The number of col , row ",len(mat_[0]),len(mat_))
    for irow in range(len(mat_)):
        print(mat_[irow])
        if(mat_[irow][0]==0):
            arr.append([0,irow])
        elif(mat_[irow][len(mat_[0])-1]==1):
            arr.append([len(mat_[0]),irow])
            print("ths",arr)
        else:
            arr.append([searchFun(mat_,irow,0,len(mat_[0])-1),irow])
    print(arr)
    arr.sort()
    
    list_=[i[1] for i in arr[:k_]]
    return list_

        


def searchInarr(arr,left,right):
    if(len(arr)==0):
        return -1+1
    if(len(arr)==1):
        if(arr[0]==1):
            return 0
        return -1+1
    mid=(left+right)//2
    if(left>right):
        return -1+1
    if(arr[mid]==1 and arr[mid+1]==0):
        return mid+1
    else:
        if(arr[mid]==0):
            return searchInarr(arr,0,mid-1)
        else:
            return searchInarr(arr,mid+1,right)
        
 
        
arr_=[1,0,0,0]

# arr_=[1,0,0,0]

# print(searchInarr(arr_,0,len(arr_)-1))


print("The",kWeakestRows(mat,k))
        
        

        
        
    
