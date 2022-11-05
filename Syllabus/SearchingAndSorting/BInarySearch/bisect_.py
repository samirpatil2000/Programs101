import bisect
#.     0. 1. 2. 3. 4. 5. 6.  7   8.  9.  10  11  12
arr = [0, 1, 2, 6, 7, 8, 12, 13, 13, 34, 56, 78]

bisect.bisect(arr, 3) # --> 3 elements
bisect.bisect(arr, 2) # --> 3 elements
bisect.bisect_left(arr, 3) # --> 3 elements
bisect.bisect_left(arr, 2) # --> 2 elements exclusive 

x = bisect.bisect_right(arr, 13) # --> 2 elements exclusive 
print(x)



# def find_element_in_range(arr, left, right):
#     print(bisect.bisect(arr, left), bisect.bisect(arr, right))
    
#     print(bisect.bisect_right(arr, right), bisect.bisect_left(arr, left))
#     return bisect.bisect_right(arr, right) - bisect.bisect_left(arr, left)

# left, right = 2, 12
# # left, right = 3, 14samir [atikl samir sapeinxm,]
# print(arr, left, right)# print(find_element_in_range(arr, left, right))asamirss