def findMin(points):
    count=0
    for i in range(len(points)-1):
        x_axis=abs(points[i+1][0]-points[i][0])
        y_axis=abs(points[i+1][1]-points[i][1])
        if(x_axis==y_axis):
            count+=x_axis
        else:
            count+=(max(x_axis,y_axis))
    return count
        
        



points = [[1,1],[3,4],[-1,0]]


print(findMin(points))