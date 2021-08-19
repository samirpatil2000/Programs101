class Solution:
    def dictStartWith(self):
        dict_={
            'samir sa':3,
            'asadsa sa':5,
            'samir sae rerg':3,
        }
        x=[k for k in dict_.keys() if k.startswith('samir')]
        print(x)
        
sol=Solution()
print(sol.dictStartWith())