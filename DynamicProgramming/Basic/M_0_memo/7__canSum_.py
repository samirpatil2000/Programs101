
def canSum(arr,target,memo={}):
    if target in memo:return memo[target]
    if target==0:return True
    if target<0: return False
    for num in arr:
        if canSum(arr,target-num):
            memo[target]=True
            return True        
    memo[target]=False
    return False

arr=[14,7]
target=300
print(canSum(arr,target))
