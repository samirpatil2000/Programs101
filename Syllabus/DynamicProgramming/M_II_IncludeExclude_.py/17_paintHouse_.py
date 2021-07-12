
arr=['157','584','329','124']
def paintHouse(arr):
    red=int(arr[0][0])
    blue=int(arr[0][1])
    green=int(arr[0][2])
    for i in range(1,len(arr)):
        temp_red=red
        temp_blue=blue
        temp_green=green
        red=min(temp_blue,temp_green)+int(arr[i][0])
        blue=min(temp_red,temp_green)+int(arr[i][1])
        green=min(temp_red,temp_blue)+int(arr[i][2])
    return min(red,blue,green)


print(paintHouse(arr ))
  
    
    