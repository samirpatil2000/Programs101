# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1

class Solution:
     
    def findLongestConseqSubseq(self, arr):
        arr.sort()
        i = 1
        max_ = 1
        while i < len(arr):
            count_ = 1
            while i < len(arr) and (arr[i] == arr[i - 1] + 1 or arr[i] == arr[i -1]):
                
                if arr[i] != arr[i - 1]:
                    count_ += 1
                
                i += 1
            i += 1
            max_ = max(count_, max_)
        return max_
    
    def findLongestConseqSubseq_UsingHash(self, arr):
        max_ = 1
        hash = set()
        for i in range(len(arr)):
            hash.add(arr[i])          
            
        for i in range(len(arr)):
            if arr[i] in hash:
                curr = arr[i]
                size = 1
                while curr + 1 in hash:
                    curr += 1
                    size += 1
                max_ = max(size, max_)
        return max_
            
                    
    
sol = Solution()
# arr = 2 6 1 9 4 5 3
arr = [2,6,1,9,4,5,3]
arr = [1,9,3,10,4,20,2]
arr = [6 ,6 ,2 ,3 ,1 ,4 ,1 ,5 ,6 ,2 ,8 ,7 ,4, 2 ,1 ,3 ,4 ,5 ,9 ,6]
# print(sol.findLongestConseqSubseq(arr))
print(sol.findLongestConseqSubseq_UsingHash(arr))