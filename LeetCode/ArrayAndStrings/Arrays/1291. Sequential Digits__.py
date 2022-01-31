


from multiprocessing.dummy import current_process
from typing import List


class Solution:
    def makeAstring(self, n: int):
        str_ = str(n)
        first_index = int(str_[0])
        if first_index + len(str_) - 1 <= 9:
            return "".join([str(first_index + i) for i in range(len(str_))])
        else:
            return "".join([str(i + 1) for i in range(len(str_) + 1)])
            
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        current_val = self.makeAstring(low)
        result = []
        if int(current_val) <= high:
            if int(current_val) >= low:
                result = [int(current_val)]
        else:
            return []
        while int(current_val) <= high:
            last_index = int(current_val[-1])
            if last_index == 9:
                current_val = "".join([str(i + 1) for i in range(len(current_val) + 1)])
            else:
                current_val = current_val[1:] + str(last_index + 1)
            if int(current_val) <= high:
                result.append(int(current_val))
            else:
                break
        return result
sol = Solution()

# print(sol.makeAstring(n = 10000))
low = 100
high = 300

low = 1000
high = 13000
low, high = 58 , 155
print(sol.sequentialDigits(low, high))