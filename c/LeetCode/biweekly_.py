def nearestValidPoint(x,y,points):
        index=-1
        min_sum=99999
        for point in points:
            print(point)
            
            if(point[0]==x or point[1]==y):
                sum=abs(x - point[0]) + abs(y - point[1])
                if(min_sum>sum):
                    min_sum=sum
                    index=min(point[1],point[0])
                elif(sum==0 or point[0]==point[1]):
                    index=0
        return index;
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]


print(nearestValidPoint(3,4,points))