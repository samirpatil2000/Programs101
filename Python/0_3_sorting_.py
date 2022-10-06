arr=[
    [1,3.00],
    [2,3.76],
    [3,3.54],
    [4,3.31],
    [5,3.32],
    [1,3.38]
    ]
x=sorted(arr,key=lambda arr:arr[1])
# print(x)
# # arr.sort(key=lambda arr:arr[0])
# print(arr)
# arr.sort(key=lambda arr:arr[0]/arr[1],reverse=True)

def sort_func(list_):
    print(list_)
    return list_[0]

    
points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2],[6,0]]

print(sorted(points, key=sort_func, reverse=True))

# print(sorted(points,key= lambda x:(-x[0],-x[1])))  #  [[6, 0], [4, 2], [3, 3], [2, 4], [2, 2], [2, 0], [1, 1]]

# print(sorted(points,key= lambda x:(x[0],-x[1])))   #  [[1, 1], [2, 4], [2, 2], [2, 0], [3, 3], [4, 2], [6, 0]]

# print(sorted(points,key= lambda x:(x[0],x[1])))   #   [[1, 1], [2, 0], [2, 2], [2, 4], [3, 3], [4, 2], [6, 0]]
# print("What output \\n do \'you\' expect?")

points = [ {0:1, 1:1}, {0:2, 1:2}, {0:2, 1:0}, {0:2, 1:4}, {0:3, 1:3}, {0:4, 1:2}, {0:6, 1:0}]

def sort_func(list_):
    return list_[0], list_[1]

# print(sorted(points,key=sort_func)) 
product = [[True, 20], [False, 20]]
print(sorted(product, key=lambda p : (-p[0], p[1])))
