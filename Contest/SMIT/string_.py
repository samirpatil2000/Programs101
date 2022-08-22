class Solution:
    
    def stream_string(self, string:str):
        result = ""
        count = 0
        hash_ = {}
        reverse_hash = {}
        min_ = 0
        for s in string:
            if s in hash_:
                x = hash_[s]
                if x != -1:
                    reverse_hash.pop(x)
                    if x == min_:
                        min_ += 1
            else:
                hash_[s] = count
                reverse_hash[count] = s
                count += 1
            result += reverse_hash.get(min_, "#")
        return result
    
sol = Solution()
string = "abadbc"
string = "abcabc"
print(sol.stream_string(string))