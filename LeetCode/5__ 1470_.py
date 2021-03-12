
def shuffle(nums,n):
    new=[0 for _ in range(2*n)]
    j=n
    k=0
    for i in range(n):
        new[k]=nums[i]
        k+=1
        new[k]=nums[j]
        # print(new)
        j+=1
        k+=1
    return new


ls=[1,2,3,4,4,3,2,1]
n = 4
print(shuffle(ls,n))