from typing import List


class Solution:
    
    def find_subsequence(self, string:str, out:str, result:List[str]):
        result[len(out)] = max(result[len(out)], out)
        if len(string) == 0:
            return
        self.find_subsequence(string[1:], out + string[0], result)
        self.find_subsequence(string[1:], out, result)
    
    def find_largest(self, string):
        result = [""] * (len(string) + 1)
        result[-1] = string
        self.find_subsequence(string, "", result)
        return result[1:]
    
    
string = "ANKI"
string[1:] # NKI
string[-1] # I
string[0]  # A


    
    
sol = Solution()
string = "abcd"
string = "dbca"
print(sol.find_largest(string))            
                