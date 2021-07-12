def numberOfWaysPrint(arr,target,list_=[]):
    if target==0:
        print(list_)
        return
    if target<0: return None
    for num in arr:
        numberOfWaysPrint(arr,target-num,list_+[num])
    return None

def numberOfWaysReturn(arr,target,memo={}):
    # if target in memo:return memo[target]
    if target==0:
        return [[]]
    if target<0: return None
    result=[]
    for num in arr:
        list_=numberOfWaysReturn(arr,target-num,memo)
        if list_!=None:
            
            for li in list_:
                
                if li!=None:
                    li.append(num)
                    result.append(li)
                    
    # memo[target]=result
    return result

target,arr=7,[5,2,3]
# target,arr=300,[3,1]
print(numberOfWaysPrint(arr,target))

x=numberOfWaysReturn(arr,target)
print(x)