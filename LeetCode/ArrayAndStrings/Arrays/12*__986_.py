

def intervalIntersection(firstList,secondList):
    i=j=0
    len_firstList=len(firstList)
    len_secondList=len(secondList)
    if(len_firstList==0 or len_secondList==0):
        return []
    list_=[]
    while(i<len_firstList and j<len_secondList):
        if(firstList[i][1]>secondList[i][1] and firstList[i][0]<secondList[i][1]):
            list_.append(secondList[i])
            i+=1
            
        elif(firstList[i][1]>=secondList[j][0] and firstList[i][0]<=secondList[j][0]):
            list_.append([secondList[j][0],firstList[i][1]])
            i+=1
        elif(firstList[i][1]<=secondList[j][0] and firstList[i][0]>=secondList[j][0]):
            list_.append([firstList[i][0],secondList[j][1]])
            j+=1
        elif(firstList[i][0]<=secondList[j][1] and firstList[i][0]>secondList[j][0]):
            list_.append([firstList[i][0],secondList[j][1]])
            j+=1
        elif(firstList[i][1]<secondList[j][0]):
            i+=1
        elif(firstList[i][1]>secondList[j][0]):
            j+=1
        # else:
        #     i+=1
        #     j+=1
    return list_



firstLIst=[[8,15]]


secondLIst=[[2,6],[8,10],[12,20]]


# firstLIst=[[14,16]]
# # [[0,2],[5,10],[13,23],[24,25]] 
# secondLIst = [[7,13],[16,20]]
# # [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(firstLIst,secondLIst))
# print([[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])