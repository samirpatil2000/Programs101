def howSum(arr,target,memo={}):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0: return None
    print(target)
    for num in arr:
        x=howSum(arr,target-num,memo)
        if x != None:
            memo[target]=x+[num]
            return memo[target]
    memo[target]=None
    return None

# target,arr=10,[5,2,3,7]
target,arr=300,[3,1]
print(howSum(arr,target))