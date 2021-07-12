import sys
from sys import stdin

def reverseFunction(nums):
    left=0
    right=len(nums)-1
    while(left<right):
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1
def func(listA,listB):
    listA.sort()
    listB.sort()
    reverseFunction(listB)
    # print(listA,listB)
    j=0
    count=0
    for i in range(len(listA)):
        if(listA[i]>listB[i]):
            count+=2
        elif(listA[i]==listB[i]):
            count+=1
    return count



# listA=[3,3,5,6,7,8]
# listB=[3,3,5,6,7,8]
# {7, 3}

def get_ints(): 
    return list(map(str, sys.stdin.readline().strip('{} }\n').split(', ')))
 
listA = get_ints()
listB= get_ints()
print(listA,listB)
listA=[int(i) for i in listA]
listB=[int(i) for i in listB]
print(func(listA,listB))

# print(listB)

