def numberOfWays(arr,target,memo={},list_=[]):
    if target==0:
        print(list_)
        return
    if target<0: return None
    for num in arr:
        numberOfWays(arr,target-num,memo,list_+[num])
    return None


target,arr=7,[5,2,3]
# target,arr=300,[3,1]
print(numberOfWays(arr,target))