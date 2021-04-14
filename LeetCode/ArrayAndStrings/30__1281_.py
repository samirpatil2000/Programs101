def subtractProductAndSum(n):
    sum=0
    prod=1
    while(n>0):
        x=n%10
        n=n//10
        sum+=x
        prod*=x
    return prod-sum
        
        # print(x,n)
        
    
print(subtractProductAndSum(4421))