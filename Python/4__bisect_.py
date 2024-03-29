import bisect
    # 0    1    2    3    4    5     6   7    8
arr = [1, 2, 6, 7, 8, 11, 34, 56, 78]
print(bisect.bisect(arr, 34)) # "7"
print(bisect.bisect(arr, 35)) # "7" 

arr_2=[[3,67],[4,7],[6,4]]
print(bisect.bisect(arr_2,[3 + 1]))


bisect.insort(arr,0)
bisect.insort(arr,13)
bisect.insort(arr,13)
print(arr)
#  0. 1. 2. 3. 4. 5. 6.  7   8.  9.  10  11  12
# [0, 1, 2, 6, 7, 8, 11, 13, 13, 34, 56, 78]

import icecream
print(bisect.bisect(arr, 13))
print(bisect.bisect_left(arr, 11))
# icecream.ic(bisect.bisect_right(arr, 11))




# print(bisect.bisect_left(arr, 56))
# print(bisect.bisect_right(arr, 56))



# arr=[1, 2, 6, 7, 8, 12]
# print(bisect.bisect(arr, 12)) 
# print(bisect.bisect(arr, 35)) 