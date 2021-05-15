def howSum(arr,target,memo={}):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0: return None
    for num in arr:
        x=howSum(arr,target-num,memo)
        if x != None:
            # new_list=x.copy()
            # new_list.append(num)
            # memo[target]=new_list
            # return new_list
            return x+[num]
    memo[target]=None
    return None

target,arr=7,[5,2,3,7]
target,arr=300,[3,1]
print(howSum(arr,target))