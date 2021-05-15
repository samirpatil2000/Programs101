
def bestSum(arr,target,memo={}):
    for target in memo:
        return memo[target]
    if target==0:return []
    if target<0:return None
    
    min_=None
    for num in arr:
        x=bestSum(arr,target-num,memo)
        if x!=None:
            combi=x.copy()
            combi+=[num]
            print(x,combi,min_)
            if min_==None or len(combi)<len(min_):
                
                min_=combi
    memo[target]=min_
    return min_
            






target,arr=7,[5,2,4,7]
# target,arr=100,[1,2,5,25]
print(bestSum(arr,target))
