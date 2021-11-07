# Input= [1,2,3] ,n=3
# Output= [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

#                                     ["1"]
                                
#                                 [1]       []
                                
#                                     ["2"]
                        
#                         [1,2]   [1]        [2]  []

#                                     ["3"]
                                
#                 [1,2,3]  [1,2]  [1,3]  [1]   [2,3]  [2]  [3] []       
                
                   

def d(arr,index=0,out=[]):
    if index==len(arr):
        print(out)
        return
    d(arr,index+1,out+[arr[index]])
    d(arr,index+1,out)
    
# a=[1,2,3]  
# d(a)

#                          d(a,0,[])
#                          /
#                      d(a,1,[1])
#                        /         \
#                d(a,2,[1,2])    d(a,2,[1])
#                 /          \ 
#         d(a,3,[1,2,3])   d(a,3,[1,2])
            
        
    
    
def rec(arr):

    if len(arr)<=1:
        return
    rec(arr[:-1])
    print(arr)
    curr=arr[-1]
    j=len(arr)-2
    while j>=0 and arr[j]>curr:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=curr


arr=[-2,-7,-1,3,4,9,-9]
rec(arr)
print(arr)