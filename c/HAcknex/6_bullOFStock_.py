

def maxProfiteBrute(list_):
    max_=0
    for i in range(len(list_)):
        for j in range(i+1,len(list_)):
            if(list_[j]-list_[i]>max_):
                max_=list_[j]-list_[i]
    return max_




def maxProfite(list_):
    min_=999999
    max_profite=0
    for i in range(len(list_)):
        min_=min(list_[i],min_)
        max_profite=max(max_profite,list_[i]-min_)
    return max_profite


arr=[7,1,5,4,6,4,3]

print(maxProfiteBrute(arr))

print(maxProfite(arr))