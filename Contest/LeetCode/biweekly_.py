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


# print(nearestValidPoint(3,4,points))

def fub(a,b):
    if (pow(a,b)>pow(b,a)):
        return a,b
    return b,a


def power_pair(list_):
    lis=[]
    for i in range(len(list_)-1):
        for j in range(i+1,len(list_)):
            if((list_[i]==1 and list_[j]==0) or (list_[i]==3 and list_[j]==2)):
                lis.append([list_[i],list_[j],pow(list_[i],list_[j]),pow(list_[j],list_[i])])
            elif(list_[j]>=list_[i] and list_[i]!=0 and list_[i]!=1):
                lis.append([list_[i],list_[j],pow(list_[i],list_[j]),pow(list_[j],list_[i])])
    return lis

print(fub(5,4))
list_=[5,1,0,3,2]
print(power_pair(list_))