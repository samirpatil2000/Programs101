from pickle import FALSE


class Solution:
    
    def product_subseq_count(self, arr, k, index, psf, added=False, memo={}):
        temp = (index, psf)
        count = 0
        if temp in memo:
            return memo[temp]
        if psf and psf <= k and added == False:
            count += 1
        if index == len(arr):
            return count
        if psf == None:
            count += self.product_subseq_count(arr, k, index + 1, 1 * arr[index], added=False, memo=memo)
        else:
            count += self.product_subseq_count(arr, k, index + 1, psf * arr[index], added=False, memo=memo)
        count += self.product_subseq_count(arr, k, index + 1, psf,  added=True, memo=memo)
        memo[temp] = count
        return count
        
        

sol = Solution()
arr = [1, 2, 3, 4]
k = 10
arr = [4, 8, 7, 2] 
k = 50
print(sol.product_subseq_count(arr, k, 0, None, ()))