class Solution:
    def intToBinary(self, num):
        return bin(num)[2:]
    def binaryToInt(self, num):
        return int(num, 2)
    
    
sol=Solution()
print(sol.intToBinary(2))
print(sol.binaryToInt("10"))