# def funt(n):
#     try:
#         if n==2:
#             return "Ok"
#     except Exception as e:
#         return str(e)
    

# print(funt("sa"))

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = ord(columnTitle[-1]) - ord('A') + 1
        i = 1
        for char in columnTitle[::-1][1:]:
            print(ord(char) - ord('A'), char, (26*(ord(char) - ord('A') + 1)), result)
            result += ((26**i)*(ord(char) - ord('A') + 1))
            i += 1
            
        return result


sol = Solution()
# columnTitle = "ZY"
# columnTitle = "FMC"
# print(sol.titleToNumber(columnTitle))
print(int("001"))