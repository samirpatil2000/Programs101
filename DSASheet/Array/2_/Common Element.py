class Solution:
    def find_min(self, arr):
        return arr.index(min(arr))
    def commonElements (self, A, B, C, n1, n2, n3):
        # your code here
        i, j, k = [0] * 3
        result = []
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] == C[j]:
                result.append(A[i])
                i += 1
                j += 1
                k += 1
            else:
                min_index = self.find_min([A[i], B[j], C[k]])
                if min_index == 0:
                    i += 1
                elif min_index == 1:
                    j += 1
                else:
                    k += 1
        return result
    
    
sol = Solution()
print(sol.commonElements(A, B, C, len(A), len(B), len(C)))