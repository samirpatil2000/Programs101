from typing import List
class Solution:
    def swap(self,arr,i,j,dict_):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        dict_[arr[i]]=i
        dict_[arr[j]]=j
        
    def minSwapsCouples(self, row: List[int]) -> int:
        dict_={}
        
        for i in range(len(row)):
            dict_[row[i]]=i
            
        swap_count_=0
        
        for i in range(0,len(row)-2,2):
            
            
            first=row[i]
            second=row[i]
            if first==0 or first%2==0:
                second+=1
            else:
                second-=1
            
            if row[i+1]!=second:
                # print(first,second,row[i+1],i)
                swap_count_+=1
                # print(row)
                self.swap(row,dict_[second],i+1,dict_)
                # print(row)
        return swap_count_
    
sol=Solution()
row=[3, 2, 0, 1]
print(sol.minSwapsCouples(row))