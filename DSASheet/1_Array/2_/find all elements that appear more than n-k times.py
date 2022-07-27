class Solution:
    
    def morethanNdK(self, arr, k):
        n = len(arr)
        if k < 2:
            return []
        hash_ = {}
        i = 0
        for i in range(len(arr)):
            if arr[i] in hash_:
                hash_[arr[i]] += 1
            else:
                if len(hash_) < k :
                    hash_[arr[i]] = 1
                for u in list(hash_.keys()):
                    hash_[u] -= 1
                    if hash_[u] == 0:
                        hash_.pop(u)
        print(hash_)     
        result = []
        for u in hash_:
            for i in range(len(arr)):
                if arr[i] == hash_[u]:
                    hash_[arr[i]] += 1
            if hash_[u] < n // k:
                result.append(u)
        return result
    
sol = Solution()
arr = [4, 5, 6, 7, 8, 4, 4]
size = len(arr)
k = 3
print(sol.morethanNdK(arr, k))        
        
                
                        
                    
            
            