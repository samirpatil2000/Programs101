from typing import List
import random

class Solution:
    
    def __init__(self, nums: List[int]):
        self.arr=nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.arr
        

    def shuffle(self) -> List[int]:
        randomArray=self.arr.copy()
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr)-1,-1,-1):
            rand_index=random.randint(0,i)
            randomArray[i],randomArray[rand_index]=randomArray[rand_index],randomArray[i]

        return randomArray
    


            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()