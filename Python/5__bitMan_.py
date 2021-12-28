class Solution:
    def intToBinary(self, num):
        return bin(num)[2:]
    def binaryToInt(self, str_num):
        return int(str_num, 2)
    
    
sol=Solution()
print(sol.intToBinary(2))
print(sol.binaryToInt("10"))

print((sol.intToBinary(5)))
print(round(3.22233,3))

"""
  101 (5)   x=5
+ 010 (2)   complement of 5
  ---
  111 (7)
+   1 (1)
  ---
 1000 (8)  ==> 2**n  n=x.bit_length()
 """