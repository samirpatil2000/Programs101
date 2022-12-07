# 
"""
Given a String we need to print each word in a string in Vertical Fashion.

Ex: String = "THIS IS A STRING"
Answer: T   I  A  S
        H   S     T
        I         R
        S         I
                  N
                  G"""

class Solution:
    
    def print_string(self, string_: str):
        string_ = string_.split()
        print(string_)
        longest_len = max([len(string_[i]) for i in range(len(string_))])
        for i in range(longest_len):
            for j in range(len(string_)):
                if len(string_[j]) > i:
                    print(string_[j][i], end="  ")
                else:
                    print("  ", end=" ")
            print()
                            
                
        
s = "THIS IS A STRING"
Solution().print_string(s)
