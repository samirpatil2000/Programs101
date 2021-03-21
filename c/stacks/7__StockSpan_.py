

def usingNGE_method(arr,n):
    new_arr=[None for _ in range(n)]
    st=[]
    new_arr[0]=1
    st.append(0)
    for i in range(1,n):
        while(len(st)>0 and arr[i]>arr[st[len(st)-1]]):
            st.pop()
        if(len(st)==0):
            new_arr[i]=i+1
        else:
            pos=st[len(st)-1]
            new_arr[i]=i-pos
        st.append(i)
    return new_arr



arr=[2,5,9,3,1,12,6,8,7]
print(usingNGE_method(arr,len(arr)))
