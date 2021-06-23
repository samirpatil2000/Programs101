#
##

####
 ###
  ##
   #
   

class Solution:
    def pattern(self,n):
        for row in range(n):
            for _ in range(0,row):
                print(" ",end=" ")
            for _ in range(row,6):
                print("# ",end="")
                
            print("\n")
            
sol=Solution()
sol.pattern(6)
            
                
            