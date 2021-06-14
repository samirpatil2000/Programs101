arr=[1,2,1,2,6]

def fun(arr):
    dict_={}
    for i in arr:
        if i in dict_:
            dict_[i]+=1
        else:
            dict_[i]=1
    # list_=zip(dict_.values(),dict_.keys())
    # list_=sorted(list_,reverse=True)
    for i in sorted(zip(dict_.values(),dict_.keys()),reverse=True):
        print(i[1],end=" ")
    print()
    
    # print(list_)
    
    
# list_=[(1,2),(2,2),(6,1)]
# list_.sort(reverse=True)
# print(list_)
fun(arr)