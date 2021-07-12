import sys
from sys import stdin, stdout


def get_ints(): 
    return list(map(str, sys.stdin.readline().strip('[] \n').split(', ')))

list_=get_ints()
n = stdin.readline()

list_=[int(j) for j in [i.replace("'","") for i in list_]]
list_.sort()

def boxGame(nums,list_):
    nums=[int(i) for i in str(nums)]
    count=0
    for i in range(len(nums)):
        if nums[i]>5:
            count+=(10-nums[i])
        else:
            count+=nums[i]
    return count

# print(list_)
print(boxGame(4218,list_))

# ['1587', '4003', '2760', '1012', '8093']
# 4218