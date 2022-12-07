class Solution:
    
    def new_greater_element(self, n: str):
        n = [i for i in n]
        i = len(n) - 2
        while i >= 0 and n[i + 1] <= n[i]:
            i -= 1
        if i == -1:
            return "Not Possible"
        smallest = i
        
        n[smallest], n[len(n) - 1] = n[len(n) - 1], n[smallest]
        return "".join(n[:smallest + 1] + sorted(n[smallest + 1:]))
        
n = "218765"
n = "1234"
n = "4321"
n = "534976"

n = "534"
print(n)
print(Solution().new_greater_element(n))
print("58" < "6")