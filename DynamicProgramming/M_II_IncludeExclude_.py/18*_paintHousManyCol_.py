
arr=['157','584','329','124']
def paintHouse(arr):
    
    red=int(arr[0][0])
    blue=int(arr[0][1])
    green=int(arr[0][2])
    
    col_arr=[int(i) for i in arr[0]]
    
    for i in range(1,len(arr)):
        temp_red=red
        temp_blue=blue
        temp_green=green
        
        temp_col_arr=col_arr.copy()
        
        for j in range(len(col_arr)):
            temp=temp_col_arr[j]
            temp_col_arr[j]=2**32
            print(col_arr[j],min(temp_col_arr),int(arr[i][j]))
            col_arr[j]=min(temp_col_arr)+int(arr[i][j])
            
            temp_col_arr[j]=temp
            print(temp_col_arr[j])
            print(col_arr[j])
            
            
        red=min(temp_blue,temp_green)+int(arr[i][0])
        blue=min(temp_red,temp_green)+int(arr[i][1])
        green=min(temp_red,temp_blue)+int(arr[i][2])
    return (red,blue,green),col_arr,


print(paintHouse(arr ))
  
    
    