from typing import NewType


def nextGreaterElement(arr,len_):
    new_arr=[None for _ in range(len_)]
    st=[]
    st.append(len_-1)
    new_arr[len_-1]=len_
    i=len_-2
    while(i>=0):
        # -A+
        while(len(st)>0 and arr[i] >=arr[st[len(st)-1]]):
            st.pop()
        if(len(st)==0):
            new_arr[i]=len_
        else:
            new_arr[i]=st[len(st)-1]
        st.append(i)
        i-=1
    return new_arr


arr=[2,5,9,3,1,12,6,8,7]


nge=nextGreaterElement(arr,len(arr))

def fun(arr,nge_arr,k):
    for i in range(len(arr)-k):
        j=i
        while(nge[j]<i+k):
            j=nge[j]
        print(arr[j])
fun(arr,nge,4)
            