

def BruteForce(arr,len_):
    new_arr=[-1 for _ in range(len_)]
    for i in range(len_-1):
        j=i+1
        while(j<len(arr)):
            while(j<len(arr) and arr[i]>arr[j]):
                j+=1
            else:
                if(j==len(arr)):
                    new_arr[i]=-1
                elif(arr[i]<arr[j]):
                    new_arr[i]=arr[j]
                break
    new_arr[len(arr)-1]=-1
    return new_arr
def usingStack(arr,len_):
    new_arr=[None for _ in range(len_)]
    # print(new_arr)
    st=[]
    st.append(arr[len_-1])
    new_arr[len_-1]=-1
    i=len_-2
    while(i>=0):
        # -A+
        while(len(st)>0 and arr[i] >=st[len(st)-1]):
            st.pop()
        if(len(st)==0):
            new_arr[i]=-1
        else:
            new_arr[i]=st[len(st)-1]
        st.append(arr[i])
        i-=1
    
    return new_arr


def usingStack_2(arr,len_):
    new_arr=[None for _ in range(len_)]
    st=[]
    st.append(0)
    for i in range(len_):
        while(len(st)>0 and arr[i]>=arr[st[len(st)-1]]):
            pos=st[len(st)-1]
            new_arr[pos]=arr[i]
            st.pop()
        st.append(i)
    
    while(len(st)>0):
        pos=st[len(st)-1]
        new_arr[pos]=-1
        st.pop()
        
    return new_arr





arr=[2,5,9,3,1,12,6,8,7]

# BruteForce(arr)
print(arr)
print(usingStack(arr,len(arr)))

print(BruteForce(arr,len(arr)))

print(usingStack_2(arr,len(arr)))