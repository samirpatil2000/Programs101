# result = [0]
# def dfs(arr1, arr2, index=0, red_sum=0, blue_sum=0, psf =""):
#     if index == len(arr1):
#         print(psf, min(red_sum, blue_sum))
#         result[0] = max(result[0], min(red_sum, blue_sum))
        
#         return
#     print(red_sum, blue_sum, index)
#     dfs(arr1, arr2, index + 1, red_sum + arr1[index], blue_sum, psf + "R"+ str(index))
#     dfs(arr1, arr2, index + 1, red_sum, blue_sum + arr2[index], psf + "B"+ str(index))
    
# def dfs_2(arr1, arr2, index=0, memo={}):
#     if index == len(arr1) - 1:
#         return (arr1[index], arr2[index])
#     a = dfs_2(arr1, arr2, index + 1, memo)
#     b = dfs_2(arr1, arr2, index + 1, memo)
#     arr = [
#         (a[0] + arr1[index], a[1]), 
#         (a[0], arr2[index] + a[1]),
#         (b[0] + arr1[index], b[1]), 
#         (b[0], arr2[index] + b[1])]
#     arr.sort(key=lambda x: min(x[0], x[1]))
#     print(arr)
#     return arr[-1]

    
    
    
    
    
arr1 = [1, 200]
arr2 = [199, 1]

# arr1 = [1, 2, 3, 10]
# arr2 = [3, 1, 3, 5]
# dfs(arr1, arr2)
# print(result[0])
# print(dfs_2(arr1, arr2))

temp = 0
print(temp^1)

print((3 + 1) // 4)