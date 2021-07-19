class Solution:
    def customSortString(self, order: str, str_: str) -> str:
        str_dict={word:str_.count(word) for word in str_}
        result=""
        for i in order:
            if i in str_dict:
                while str_dict[i]>0:
                    result+=i
                    str_dict[i]-=1
        print(str_dict)
        for i in str_dict.keys():
            while str_dict[i]>0:
                result+=i
                str_dict[i]-=1
              
            
        return result        
        
sol=Solution()
order = "cba"
str = "abcd"
order="cbafg"
str="abcd"
order="hucw"
str="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
print(sol.customSortString(order,str))