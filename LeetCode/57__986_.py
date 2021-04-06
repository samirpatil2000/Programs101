
def intervalIntersection(firstList, secondList):
    i=j=0
    len_firstList=len(firstList)
    len_secondList=len(secondList)
    if(len_firstList==0 or len_secondList==0):
        return []
    list_=[]
    
    while(i<len_firstList and j<len_secondList):
        # print(firstList[i][0],secondList[j][1])
        if(firstList[i][0]<secondList[j][1] and firstList[i][1]>=secondList[j][0]):
            list_.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
            if(firstList[i][1]<secondList[j][1]):
                i+=1
            elif(firstList[i][1]>secondList[j][1]):
                j+=1
            else:
                i+=1
                j+=1
        elif(firstList[i][0]<secondList[j][1] and firstList[i][1]<secondList[j][0]):
            i+=1
        elif(firstList[i][0]==secondList[j][1]):
            list_.append([firstList[i][0],secondList[j][1]])
            j+=1
        else:
            j+=1
            
    return list_

firstList = [[10,12],[18,19]]
secondList = [[1,6],[8,11],[13,17],[19,20]]

print(intervalIntersection(firstList,secondList))
        
    