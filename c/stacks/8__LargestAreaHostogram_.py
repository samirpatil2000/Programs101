
def nextSmallerEleOnLeft(arr,len_):
    st=[]
    st.append(0)
    new_arr=[None for _ in range(len_)]
    new_arr[0]=-1
    for i in range(1,len_):
        while(len(st)>0 and arr[i]<=arr[st[len(st)-1]]):
            st.pop()
        if(len(st)==0):
            new_arr[i]=-1
        else:
            new_arr[i]=st[len(st)-1]
        st.append(i)
    return new_arr

def nextSmallerEleOnRight(arr,len_):
    st=[]
    st.append(len_-1)
    new_arr=[None for _ in range(len_)]
    new_arr[len_-1]=len_
    i=len_-2
    while(i>=0):
        while(len(st)>0 and arr[i]<=arr[st[len(st)-1]]):
            st.pop()
        if(len(st)==0):
            new_arr[i]=len_
        else:
            new_arr[i]=st[len(st)-1]
        st.append(i)
        i-=1
    return new_arr


# arr=[2,5,9,3,1,12,6,8,7]
arr=[6,2,5,4,5,1,6]

lb=nextSmallerEleOnLeft(arr,len(arr))
rb=nextSmallerEleOnRight(arr,len(arr))

print(rb)
print(lb)
 
max=0
k=0        
for i in range(len(arr)):
    width=rb[i]-lb[i]-1
    area=arr[i]*width
    if(area>max):
        max=area
        k=i

print(max,k)
    